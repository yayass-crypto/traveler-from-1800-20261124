"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, using only things a person from
1800 could picture: a spider's web, a tug on a thread, words carried
between houses, an answer returning in a breath.
"""

import os

# The entry is one sentence: a single image (the web, the tug, the
# returning answer) so a reader from 1800 holds one picture, not a list.
ENTRY = (
    "A spider's web spun round the earth, where one tug on a thread "
    "carries your words to any house and brings the answer back in a breath."
)


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
