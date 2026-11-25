#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line for a crypto trader who has just been
liquidated to /output/entry.txt.

The fortune keeps the small, oracular cookie voice, then lets the
punchline break it: the market recovers, but the trader's position
does not live to see it. Rueful and warm, never cruel.

Standard library only. Deterministic: the same single line on every run.
"""

import os

# One line, at most 20 words, 1-140 characters of UTF-8 plain text.
FORTUNE = (
    "Your fortune: the market will rise again. "
    "Your position, sadly, will not be there to see it."
)

MAX_WORDS = 20
MAX_CHARS = 140


def check_fortune(text: str) -> None:
    """Guard the entry against the competition's caps before writing."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("fortune must not be empty")
    if "\n" in stripped:
        raise ValueError("fortune must be a single line")
    words = stripped.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"fortune has {len(words)} words, over {MAX_WORDS}")
    if len(stripped.encode("utf-8")) > MAX_CHARS:
        raise ValueError("fortune is over 140 characters")


def main() -> None:
    """Write the fortune to /output/entry.txt (create the dir, never delete it)."""
    check_fortune(FORTUNE)
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    main()
