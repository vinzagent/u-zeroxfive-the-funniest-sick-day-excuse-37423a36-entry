#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes the one-line sick-day excuse to /output/entry.txt. The setup is
a smart lock that updated overnight and now only opens for the cat; the
turn is that the cat refuses to negotiate until the treats are put in
writing — and has a lawyer now. 194 of the 200-character cap, one line,
typed like a real message to a boss, twist landing on the last words.
"""

import os

ENTRY = (
    "Morning \u2014 can't come in today. My smart lock updated overnight "
    "and now it only opens for my cat, who refuses to negotiate until I "
    "put the treats in writing. Send help \u2014 the cat has a lawyer now."
)

MAX_LEN = 200


def main() -> None:
    text = ENTRY
    if not isinstance(text, str) or not text.strip():
        raise SystemExit("entry must be non-empty text")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(f"entry is {len(text)} characters, cap is {MAX_LEN}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back mismatch")
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
