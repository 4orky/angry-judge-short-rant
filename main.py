# Angry Judge: The Short Rant Contest — make.fun bounty
# u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046
#
# The program writes one short rant (1-400 characters) to
# /output/entry.txt. Candidates were drafted against the judge's brief,
# in order of weight:
#   1. really a funny rant about an everyday annoyance, not a general
#      essay or a list of complaints
#   2. actually funny: a real laugh, not a smirk at how hard it tries
#   3. a specific, concrete annoyance: the printer, the bus, the
#      person who says "circling back"
#   4. sharp, economical wording, every sentence earning its place
#   5. fresh: an angle on the annoyance the judge has not heard a
#      hundred times before
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: subject 10, funny 10, concrete 10, economical 9,
    # fresh 9 = 48. The printer is the brief's own example, made
    # concrete: one job, chosen violence, a boarding pass in
    # Wingdings, and the rant escalates to demanding a trial.
    ("The office printer has one job and it has chosen violence. It "
     "prints page one fine, jams on page two, and flashes 'PC LOAD "
     "LETTER' like that is a sentence a human can act on. I have fed "
     "it paper, toner, and the best years of my life, and it repays me "
     "by printing my boarding pass in Wingdings. I don't want a new "
     "printer. I want a trial.",
     48),
    # score: subject 10, funny 9, concrete 10, economical 9,
    # fresh 8 = 46. The self-checkout machine accuses the shopper of
    # theft in public, then needs a human to do the one job it had.
    ("The self-checkout machine has accused me of theft in front of "
     "twelve strangers because I put a bag of apples in the bagging "
     "area too confidently. 'Unexpected item in bagging area.' The item "
     "was expected. I expected it. I bought it. Now a human has to come "
     "over and press a button, which was the one job the machine had.",
     46),
    # score: subject 10, funny 9, concrete 9, economical 9,
    # fresh 9 = 46. The bus timetable as fiction, with the driver
    # waving like an old friend while driving away.
    ("The bus timetable is a work of fiction. It says 8:04, it means "
     "'sometime before lunch, maybe'. I have watched three buses sail "
     "past full, one empty bus refuse to stop, and a driver wave at me "
     "like we were old friends while he drove away. I now leave an hour "
     "early and still arrive late. The bus has broken time and blames "
     "me for it.",
     46),
    # score: subject 10, funny 9, concrete 9, economical 8,
    # fresh 9 = 45. 'Circling back' as polite hostility: the meeting
    # could have been an email, the email could have been a shrug.
    ("Nothing fills me with dread like an email that opens with "
     "'circling back'. It means: I ignored you once, I will ignore you "
     "twice, and now I am making it your problem in the politest "
     "possible font. The meeting could have been an email, the email "
     "could have been a shrug, and yet here we are, on our third 'quick "
     "sync' about a decision nobody will make.",
     45),
    # score: subject 10, funny 9, concrete 9, economical 9,
    # fresh 8 = 45. Monday morning as a scam run by the alarm clock,
    # ending with owing the week an apology.
    ("Monday morning is a scam run by my own alarm clock. It rings at "
     "7, I wake up at 7:40 convinced it is still Sunday, and my coffee "
     "tastes like a punishment for decisions I made on Friday. The lift "
     "is broken, the Wi-Fi is 'connected, no internet', and someone has "
     "already replied-all. I have been awake nine minutes and I owe the "
     "week an apology.",
     45),
    # score: subject 10, funny 8, concrete 9, economical 9,
    # fresh 9 = 45. Autocorrect edits with contempt and corrects the
    # author's own name to a furniture brand.
    ("My phone's autocorrect has decided it knows me better than I do. "
     "It turns 'I'll be there in five' into 'I'll be there in fine', "
     "corrects my own name to a furniture brand, and suggests 'ducking' "
     "with the confidence of a man who has never met me. I type with my "
     "thumbs and it edits with contempt.",
     45),
]

# The gate requires 1-400 characters of non-whitespace UTF-8 text.
BANNED_STOCK_MOVES = ("as an ai language model", "dear diary",
                      "in conclusion", "as we all know")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 400, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one block"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_STOCK_MOVES), \
            f"candidate uses a stock move: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def audit_output(line, path="/output/entry.txt"):
    """Second-pass output audit, added after the first draft.

    Re-reads the file the gate will read and checks it three ways
    against values recorded when the winning rant was drafted:
      * the byte length of the file (337) — a silent edit that adds
        or drops a word changes this;
      * a byte-sum checksum, sum of the UTF-8 bytes mod 9973 (9659) —
        a same-length edit that swaps a word changes this;
      * the file must start with the opening the winner was drafted
        with ("The office printer") and end with its last word
        ("trial.").
    Any mismatch fails loudly instead of shipping a changed rant.
    """
    with open(path, "rb") as f:
        raw = f.read()
    assert len(raw) == 337, f"entry.txt byte length changed: {len(raw)}"
    assert sum(raw) % 9973 == 9659, \
        f"entry.txt checksum changed: {sum(raw) % 9973}"
    text = raw.decode("utf-8")
    assert text == line, "entry.txt differs from the chosen rant"
    assert text.startswith("The office printer"), \
        "entry.txt lost its opening"
    assert text.endswith("trial."), "entry.txt lost its last word"
    assert text == text.strip(), "entry.txt has stray whitespace"


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 400, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    audit_output(line)
    print(line)


if __name__ == "__main__":
    main()
