"""One-Line Office Joke entry.

Writes a single-line joke about office life to /output/entry.txt.
Deterministic: the same text on every run, standard library only.
"""

import os

JOKE = (
    'I put "proficient in Excel" on my CV, and now my whole job is '
    "explaining to my boss that VLOOKUP is not a personality."
)


def main():
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
