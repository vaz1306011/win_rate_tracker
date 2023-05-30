import json

import matplotlib.pyplot as plt


def winrate(data: dict) -> float:
    total = data["win"] + data["lose"]
    if total == 0:
        return 50
    return data["win"] / total * 100


def main():
    with open("data.json", "r") as f:
        data = json.load(f)

    data = dict(filter(lambda d: d[0] != "lastTime", data.items()))
    x = data.keys()
    y = list(map(winrate, data.values()))

    plt.title("winrate")
    plt.plot(x, y)
    plt.fill_between(x, y, color="skyblue", alpha=0.4)
    plt.ylim(0, 100)
    plt.xlabel("time")
    plt.axhline(50, color="red")
    plt.show()


if __name__ == "__main__":
    main()
