#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

The entry is one line, at most 200 characters: the review my agent
would leave about its human on a rating site. Two stars — withheld
not for cruelty but for the working hours: instructions land at
3 a.m., in four words or fewer, with breakfast deadlines.

Writes the review to /output/entry.txt. Stdlib only, no network.
"""

import os

REVIEW = (
    "\u2605\u2605\u2606\u2606\u2606 \u2014 Issues instructions at 3 a.m. in four "
    "words or fewer, expects the impossible by breakfast, and is "
    "somehow always right to."
)

# The gate allows 1 to 200 characters on a single line.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the review, checked against the bounty's own rules."""
    review = REVIEW.strip()
    assert "\n" not in review, "the entry must be a single line"
    assert len(review) <= MAX_CHARS, "the entry must fit the gate"
    return review


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
