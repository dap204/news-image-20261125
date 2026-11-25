// The World Today — 25 November 2026 · make.fun news-image-20261125
//
// The front page is drawn by draw.py (Python + Pillow, system DejaVu
// fonts, no network) and ships in this repository as entry.b64 — the
// PNG as base64 text, wrapped at 4000 characters a line, so the whole
// repository stays plain text. This file is only the delivery step:
// it unfolds entry.b64 back into the exact PNG bytes, checks the
// result really is a PNG, and writes it where the grader looks:
//
//   MAKEFUN_OUTPUT_DIR=<dir> node main.ts      (local runs)
//   node main.ts                               (grader: /output)
//
// Node 22, standard library only, no network. The output is a pure
// function of entry.b64, so two runs always write identical bytes.

import { mkdirSync, readFileSync, writeFileSync, chmodSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const outFile = join(outDir, "entry.png");

const b64 = readFileSync(join(here, "entry.b64"), "utf8").replace(/\s+/g, "");
const png = Buffer.from(b64, "base64");

// Sanity checks: PNG signature up front, IEND chunk at the end.
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!png.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.b64 does not decode to a PNG (bad magic)");
}
if (!png.subarray(png.length - 12).includes(Buffer.from("IEND"))) {
  throw new Error("entry.b64 does not decode to a PNG (no IEND trailer)");
}
if (png.length > 1024 * 1024) {
  throw new Error(`decoded PNG is ${png.length} bytes, over the 1 MiB cap`);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(outFile, png);
chmodSync(outFile, 0o644);
console.log(`wrote ${outFile} (${png.length} bytes)`);
