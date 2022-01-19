from datetime import datetime
import logging
from pathlib import Path
import random
import os
import sys
from typing import Literal, Optional

logger = logging.getLogger(__name__)
HERE = Path(__file__).parent.resolve()

GREEN = "🟩"
YELLOW = "🟨"
RED = "🟥"
CORRECT_PATTERN = [GREEN, GREEN, GREEN, GREEN, GREEN]
Color = Literal[GREEN, YELLOW, RED]

INSTRUCTIONS = f"""Input 5 characters word.
{GREEN}: Collect character
{YELLOW}: Character is collect, but place is wrong
{RED}: Character is not included in the answer
"""


def load_corpus(seed: int) -> str:
    random.seed(seed)
    with open((HERE / "var/corpus.txt"), "r") as f:
        words = f.readlines()
    correct = random.choice(words).strip("\n")
    return correct


def check(got: str, correct: str) -> list[Color]:
    result = []
    for i, token in enumerate(got):
        if token == correct[i]:
            color = GREEN
        elif token in correct:
            color = YELLOW
        else:
            color = RED
        result.append(color)
    print("".join(result))
    return result


def challenge(correct: str, i: int = 1, progress: Optional[list[str]] = None):
    if progress is None:
        progress = []

    got = input(f"Challenge {i}:").strip()
    if len(got) != 5:
        print("Please input 5 characters word")
        return challenge(correct, i, progress)

    result = check(got, correct)
    progress.append("".join(result))

    if result == CORRECT_PATTERN:
        print(f"\n\nSucceed! challenge: {i}/5")
        print("\n".join(progress))
        sys.exit(0)
    elif i >= 5:
        print("\n\nFailed")
        print("\n".join(progress))
        sys.exit(1)
    else:
        challenge(correct, i + 1, progress)


def main():
    seed = datetime.today().toordinal()
    correct = load_corpus(seed)
    logger.debug("Today's answer: %s, seed: %d", correct, seed)
    print(INSTRUCTIONS)
    while True:
        challenge(correct, i=1)


if __name__ == "__main__":
    if os.environ.get("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
    main()
