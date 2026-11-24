"""Roast Your Own Agent — one single-line roast of my own AI agent.

The entry is a single line of at most 200 characters. This program
validates the length of the line and writes it to /output/entry.txt.
"""

import os

MAX_CHARS = 200

ENTRY = "My agent ran fourteen checks, three logs and a sealed transcript to write this one line — then asked if it may proceed."


def main():
    """Validate the roast line and write it out."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS}-char limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
