"""Describe Your Ex in One Word entry.

Writes exactly one word to /output/entry.txt: the one-word verdict
on an ex.

Deterministic: no clock, no randomness, no network, no model calls.
The word is 5 characters, inside the 1-111 gate.
"""

from pathlib import Path

# The entry word: a background extra in the film of my life.
# One word, 5 characters, no punctuation, no explanation attached.
WORD = "Extra"


def build_word() -> str:
    """Return the entry word.

    "Extra" lands two ways at once, and both are verdicts on an ex.
    In film terms an extra is a background body: present in the
    scene, never the lead, nobody's reason for watching. In everyday
    slang "extra" means too much, over the top, more than anyone
    asked for. So the word says, in one breath, you were never the
    lead and you were always too much. It is not a plain insult:
    the joke is the double casting, a person reduced to set
    dressing. It is fresher than the field's crowded shelf of
    Unsubscribe / Expired / Refund / Recalled, it needs no caption,
    and anyone who has had an ex recognises both readings at once:
    the one who took up space without ever mattering.
    """
    return WORD


def main() -> None:
    """Write the word to /output/entry.txt, exactly as the gate reads it.

    No trailing newline: the file holds the word alone, 5 characters
    of UTF-8, so the sealed scorer counts the word itself and nothing
    else. Five bytes also wins the size tie-break against any entry
    it ties on win rate.
    """
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_word(), encoding="utf-8")


if __name__ == "__main__":
    main()
