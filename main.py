"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word my ex would
use to describe me. Pure Python standard library, no dependencies.
"""

import os

ENTRY = "Clingy"
OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 24


def validate(text: str) -> str:
    """Check the entry against the competition gate and return it.

    The gate requires /output/entry.txt to hold UTF-8 text of 1 to 24
    characters, not only white space. The task adds one more rule of
    its own: exactly one word, nothing else.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise ValueError(
            "entry must be %d-%d characters, got %d" % (MIN_LEN, MAX_LEN, len(text))
        )
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word, got %r" % text)
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: the file must hold exactly what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("read-back mismatch: wrote %r, file holds %r" % (text, written))
    print(text)


if __name__ == "__main__":
    main()
