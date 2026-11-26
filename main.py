import os

LINE = "Competitive apologising: two rivals say sorry until one of them actually means it. The first to stop apologising is disqualified."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
