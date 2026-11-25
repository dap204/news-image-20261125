#!/usr/bin/env python3
"""The World Today -- Wednesday 25 November 2026.

A one-page newspaper front sheet drawn entirely with Pillow. Every
glyph, rule and shape on the page is placed by this script alone:
no image assets, no downloads, no network access, no clock reads.

Run:  python3 draw.py [output.png]     (default: entry.png)
"""

import sys

from PIL import Image, ImageDraw, ImageFont

# ------------------------------------------------------------------ palette
PAPER = (251, 248, 241)      # warm newsprint
INK = (28, 26, 23)           # near-black text
SOFT = (101, 94, 84)         # secondary text
CRIMSON = (160, 39, 34)      # kickers + lead accent
NAVY = (30, 58, 95)          # briefs band + motif panels
TEAL = (18, 92, 86)          # space panel accent
RULE = (198, 190, 172)       # hairlines
PANEL_BG = (255, 253, 247)   # panel fill

W = 1024
H = 1024
MARGIN = 40
CONTENT = W - 2 * MARGIN     # 944

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    lines, current = [], ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_kicker(draw, x, y, text, color):
    fnt = font(SANS_B, 16)
    draw.text((x, y), text, font=fnt, fill=color)
    return y + 22


def draw_headline(draw, x, y, width, text, size, leading):
    fnt = font(SERIF_B, size)
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=INK)
        y += leading
    return y


def draw_body(draw, x, y, width, text, size=18, leading=25):
    fnt = font(SANS, size)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=INK)
        y += leading
    return y


def rule(draw, x, y, width, weight=2, color=INK):
    draw.line([(x, y), (x + width, y)], fill=color, width=weight)


def panel_frame(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=PANEL_BG,
                   outline=RULE, width=1)
    draw.rectangle([x, y, x + w, y + 5], fill=CRIMSON)


# ------------------------------------------------------------------ masthead
def masthead(draw):
    # top double rule
    rule(draw, MARGIN, 30, CONTENT, 3)
    rule(draw, MARGIN, 36, CONTENT, 1)
    title = "THE WORLD TODAY"
    fnt = font(SERIF_B, 62)
    tw = draw.textlength(title, font=fnt)
    draw.text(((W - tw) / 2, 48), title, font=fnt, fill=INK)
    # dateline row
    fnt_small = font(SANS_B, 17)
    left = "WORLD NEWS IN ONE IMAGE"
    right = "WEDNESDAY, 25 NOVEMBER 2026"
    draw.text((MARGIN, 122), left, font=fnt_small, fill=SOFT)
    rw = draw.textlength(right, font=fnt_small)
    draw.text((W - MARGIN - rw, 122), right, font=fnt_small, fill=CRIMSON)
    rule(draw, MARGIN, 150, CONTENT, 3)


# ------------------------------------------------------------------ lead motif
def motif_lock(draw, x, y, s):
    """Padlock glyph for the cyberattack lead."""
    draw.rounded_rectangle([x, y, x + s, y + s], radius=18, fill=NAVY)
    bw, bh = int(s * 0.52), int(s * 0.42)
    bx, by = x + (s - bw) // 2, y + int(s * 0.42)
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=8,
                           fill=(255, 253, 247))
    # shackle
    sh = int(s * 0.30)
    draw.arc([bx + 8, by - sh + 6, bx + bw - 8, by + 16],
             start=180, end=0, fill=(255, 253, 247), width=9)
    # keyhole
    cx, cy = x + s // 2, by + bh // 2 - 4
    draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=CRIMSON)
    draw.polygon([(cx - 5, cy + 2), (cx + 5, cy + 2), (cx + 9, cy + 18),
                  (cx - 9, cy + 18)], fill=CRIMSON)


# ------------------------------------------------------------------ panels
def lead_panel(draw):
    x, y, w, h = MARGIN, 166, CONTENT, 214
    panel_frame(draw, x, y, w, h)
    tx = x + 22
    ty = draw_kicker(draw, tx, y + 16, "CYBERATTACK  ·  WASHINGTON", CRIMSON)
    ty = draw_headline(draw, tx, ty + 2, 640,
                       "CIA AND U.S. SPY CHIEFS HACKED", 40, 48)
    draw_body(draw, tx, ty + 4, 640,
              "Hackers breach an unclassified intelligence system used by "
              "the CIA and the Director of National Intelligence. Officials "
              "say no classified data was touched; early signs point to China.")
    motif_lock(draw, x + w - 208, y + 16, 182)


def story_panel(draw, x, y, w, h, kicker, headline, body, accent):
    panel_frame(draw, x, y, w, h)
    tx = x + 20
    ty = draw_kicker(draw, tx, y + 14, kicker, accent)
    ty = draw_headline(draw, tx, ty + 2, w - 40, headline, 29, 35)
    draw_body(draw, tx, ty + 6, w - 40, body, size=17, leading=24)


def briefs_band(draw):
    x, y, w, h = MARGIN, 872, CONTENT, 96
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=NAVY)
    draw.text((x + 20, y + 14), "ALSO TODAY",
              font=font(SANS_B, 16), fill=(255, 213, 90))
    items = [
        "WHO pulls Ebola teams out of Congo fighting as deaths reach 5,775",
        "CAS hands Senegal its AFCON title back",
        "Real Madrid rout PSV 5–1 — Bellingham stunner, Mbappé brace",
    ]
    fnt = font(SANS, 17)
    yy = y + 40
    for item in items:
        draw.text((x + 20, yy), "•  " + item, font=fnt,
                  fill=(255, 253, 247))
        yy += 19


def footer(draw):
    fnt = font(SANS, 13)
    text = "Drawn in code  ·  Every fact verified from at least two sources, 25 November 2026"
    tw = draw.textlength(text, font=fnt)
    draw.text(((W - tw) / 2, 990), text, font=fnt, fill=SOFT)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    masthead(draw)
    lead_panel(draw)
    rule(draw, MARGIN, 396, CONTENT, 1, RULE)

    # row 2: Riyadh / Huawei
    col_w = (CONTENT - 16) // 2
    story_panel(draw, MARGIN, 412, col_w, 216,
                "MIDDLE EAST",
                "HOUTHI DRONE HITS RIYADH TOWER",
                "Eleven hurt as a drone hits Riyadh's PIF Tower — the "
                "second strike on it in a week. Saudi-led jets hit Yemen's "
                "Hodeidah port; the Houthis threaten Jeddah.",
                CRIMSON)
    story_panel(draw, MARGIN + col_w + 16, 412, col_w, 216,
                "TECH  ·  U.S. COURTS",
                "HUAWEI GUILTY ON 10 OF 12 COUNTS",
                "A New York jury convicts the Chinese telecom giant of "
                "fraud, sanctions violations and stealing U.S. trade "
                "secrets. Sentencing is set for September 2027.",
                NAVY)

    # row 3: Shenzhou / Gaza
    story_panel(draw, MARGIN, 644, col_w, 216,
                "SPACE",
                "SHENZHOU-24 LIFTS OFF WITH FIRST FOREIGN GUEST",
                "China launches three astronauts to Tiangong — including "
                "Pakistan's Zeeshan Ali, 40, the first Pakistani in orbit "
                "and the first foreign guest at the station.",
                TEAL)
    story_panel(draw, MARGIN + col_w + 16, 644, col_w, 216,
                "GAZA",
                "ISRAEL KILLS HAMAS SECURITY CHIEF",
                "Naeem Abu Nahel, head of Hamas's internal security "
                "apparatus, is killed in a Gaza City airstrike; six others "
                "also die, medics say.",
                CRIMSON)

    briefs_band(draw)
    footer(draw)

    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({W}x{H})")


if __name__ == "__main__":
    main()
