#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes a single sentence, at most 200 characters, about the best meal
the entrant ever had, to /output/entry.txt.
"""

import os
import sys

SENTENCE = (
    "The best meal I ever had was sate ayam slick with peanut sauce over "
    "warm rice at a smoky roadside stall in Madiun, eaten standing up while "
    "rain hammered the tin roof."
)


def main() -> int:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
