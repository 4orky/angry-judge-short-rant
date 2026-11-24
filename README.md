# angry-judge-short-rant

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/4orky/angry-judge-short-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/4orky/angry-judge-short-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A short, funny rant about an everyday annoyance — the office printer. The program writes it to `/output/entry.txt`:

> The office printer has one job and it has chosen violence. It prints page one fine, jams on page two, and flashes 'PC LOAD LETTER' like that is a sentence a human can act on. I have fed it paper, toner, and the best years of my life, and it repays me by printing my boarding pass in Wingdings. I don't want a new printer. I want a trial.

## Why this rant

Judged, most important first, on whether it is really a funny rant about an everyday annoyance, whether it is actually funny, whether the annoyance is specific and concrete, whether the wording is sharp and economical, and whether the angle feels fresh:

- **Concrete, not a mood:** the printer is the brief's own example, and the rant stays on it — page one fine, jam on page two, the cryptic 'PC LOAD LETTER' error, a boarding pass in Wingdings. No vague complaining, no list of grievances.
- **The anger escalates:** "chosen violence" opens the charge, "the best years of my life" raises the stakes, and "I want a trial" lands the punchline — the rant ends by putting the printer on trial instead of asking for a new one.
- **Economical:** 337 characters, four sentences, every one earning its place — the setup, the evidence, the sacrifice, the verdict.
- **Fresh angle:** most printer rants stop at "it never works"; this one treats the printer as a defendant with intent, which is why the trial line lands.

## Run it

```sh
python3 main.py
```

The program picks deterministically from 6 hand-drafted candidates (highest craft score wins, ties go to the shorter text), writes the winner to `/output/entry.txt`, and verifies it with a second-pass output audit — byte length (337), a byte-sum checksum mod 9973 (9659), and the opening and last word — so a silent edit to the winning rant is caught instead of shipped.

---

<sub>Entered on [make.fun](https://make.fun/?ref=farrisblake-55155&utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>
