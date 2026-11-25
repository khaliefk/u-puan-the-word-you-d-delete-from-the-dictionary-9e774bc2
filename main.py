#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes exactly one word to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set): Monday.

Everyone hates Monday. It is the day the weekend dies, the alarm wins,
and the week starts whether you are ready or not. Erase the word and the
day still shows up on the calendar, but at least nobody can name it
anymore. That is the whole joke, and it lands the moment you read it.
"""

import os

WORD = "Monday"  # the word to erase from the dictionary forever
MAX_CHARS = 77

if not 1 <= len(WORD) <= MAX_CHARS:
    raise ValueError(f"WORD must be 1-{MAX_CHARS} characters, got {len(WORD)}")
if len(WORD.split()) != 1:
    raise ValueError(f"WORD must be exactly one word, got {WORD!r}")


def validate_word(word: str) -> None:
    """Self-check: exactly one word, one line, inside the 1-77 gate."""
    if not 1 <= len(word) <= MAX_CHARS:
        raise ValueError(f"WORD must be 1-{MAX_CHARS} characters, got {len(word)}")
    if len(word.split()) != 1 or "\n" in word or "\r" in word:
        raise ValueError(f"WORD must be a single word on one line, got {word!r}")


def main() -> None:
    validate_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError(f"read-back mismatch: wrote {WORD!r}, file holds {written!r}")
    print(f"wrote {path}: {WORD!r} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()
