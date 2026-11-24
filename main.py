#!/usr/bin/env python3
"""One Word for Your Wi-Fi: the entry program.

Writes a single word describing home Wi-Fi to /output/entry.txt.
Pure stdlib only.
"""

import os

# PART_A: the entry word, one word only.
WORD = "diva"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main():
    # PART_B: gate guard — 1-20 chars, a single word, no whitespace.
    assert 1 <= len(WORD) <= 20, "word must be 1-20 chars"
    assert WORD == WORD.strip() and not any(c.isspace() for c in WORD), \
        "word must be a single word with no whitespace"
    word = WORD
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
