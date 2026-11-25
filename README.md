# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/dap204/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/dap204/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty
[news-image-20261125](https://make.fun/bounty/news-image-20261125):
sum up the world's news of Wednesday 25 November 2026 in one image.

A flat, code-drawn newspaper front page, 1024×1024 PNG. The picture is
drawn by `draw.py` (Python + Pillow, system DejaVu fonts, no network, no
external assets); its output travels in this repository as `entry.b64`
(base64, 4000-character lines) so the repo stays plain text end to end.
`main.ts` (Node 22, standard library only) decodes `entry.b64`, checks the
PNG magic and IEND trailer, and writes the bytes to `/output/entry.png`
(or `$MAKEFUN_OUTPUT_DIR` locally). Two runs always write identical bytes.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Regenerate the picture:

```sh
python3 draw.py   # writes entry.png; re-encode to entry.b64 afterwards
```

## The day's news, as drawn

Every fact was re-verified by web search on the afternoon of 25 November
2026 (WITA) before drawing:

1. **CIA and U.S. spy chiefs hacked (lead).** Hackers breached an
   unclassified intelligence system used by the CIA and the Office of the
   Director of National Intelligence for open-source analysis. Officials
   say no classified data was touched; early indications point to China.
   (CNN — first reported by the NYT; Reuters, AP, Fox)
2. **Houthi drone hits Riyadh tower.** Eleven people hurt as a drone hit
   Riyadh's PIF Tower, the second strike on it in a week. The Saudi-led
   coalition hit Yemen's Hodeidah port after an evacuation warning; the
   Houthis threatened Jeddah and all Saudi Red Sea ports.
   (Reuters/TBS, Arab News, WION)
3. **Huawei guilty on 10 of 12 counts.** A federal jury in Brooklyn
   convicted the Chinese telecom giant of fraud, sanctions violations and
   stealing U.S. trade secrets; acquitted of racketeering. Sentencing set
   for 14 September 2027. (Reuters, CNN, U.S. Department of Justice)
4. **Shenzhou-24 lifts off.** China launched three astronauts to its
   Tiangong station — including Pakistan's Muhammad Zeeshan Ali, 40, the
   first Pakistani in orbit and the first foreign visitor to the station.
   (Reuters, Xinhua)
5. **Israel kills Hamas security chief.** Naeem Abu Nahel, head of Hamas's
   internal security apparatus, was killed in a Gaza City airstrike; six
   others also died, medics said. (Reuters, Times of Israel)
6. **Also today.** WHO pulled Ebola teams out of Congo fighting as the
   death toll reached 5,775; CAS handed Senegal its AFCON title back;
   Real Madrid routed PSV 5–1 (Bellingham stunner, Mbappé brace).

Dropped during verification: the Indonesia vice-president resignation
(12 Nov — old news, not 25 Nov) and the unverified Banten factory fire.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tedem4sj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
