"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word my ex would
use to describe me. Pure Python standard library, no dependencies.
"""

import os

ENTRY = "Clingy"
OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 24


def main() -> None:
    text = ENTRY
    # Gate guard: 1-24 chars, a single word, not whitespace-only.
    assert MIN_LEN <= len(text) <= MAX_LEN, "entry out of range"
    assert text.strip() != "", "entry is whitespace-only"
    assert len(text.split()) == 1, "entry must be exactly one word"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: the file must hold exactly what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "read-back mismatch"
    print(text)


if __name__ == "__main__":
    main()
