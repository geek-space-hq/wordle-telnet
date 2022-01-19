import urllib.request
from pathlib import Path

HERE = Path(__file__).parent.resolve()
URL = "https://www.wordfrequency.info/samples/lemmas_60k.txt"


def main():
    with urllib.request.urlopen(URL) as f:
        data: str = f.read().decode("utf-8")
    all_words = [row.split("\t")[1] for row in data.splitlines()[9:]]
    words_5chars = [s for s in all_words if s.isalpha() and len(s) == 5]
    with open((HERE.parent / "var" / "corpus.txt"), "w") as f:
        f.write("\n".join(words_5chars))


if __name__ == "__main__":
    main()
