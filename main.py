#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry for make.fun.

Writes a single word to /output/entry.txt. Deterministic:
no input, no network, no randomness — the same word every run.
"""

from pathlib import Path


def main() -> None:
    # One word, exactly five characters, no trailing newline.
    word = "Extra"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
