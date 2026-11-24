"""Monday, reviewed in one line.

Loads the single-line Monday review from entry.txt and prints it.
"""

import pathlib


def load_review() -> str:
    review_path = pathlib.Path(__file__).with_name("entry.txt")
    lines = review_path.read_text(encoding="utf-8").strip().splitlines()
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one line")
    return lines[0]


def main() -> None:
    print(load_review())


if __name__ == "__main__":
    main()
