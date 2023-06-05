import json

import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor


def winrate(data: dict) -> float:
    total = data["win"] + data["lose"]
    if total == 0:
        return 50
    return data["win"] / total * 100


def main():
    with open("data.json", "r") as f:
        data = json.load(f)
        lastTime = data["lastTime"]

    data = dict(filter(lambda d: d[0] != "lastTime", data.items()))
    x = data.keys()
    y = list(map(winrate, data.values()))

    plt.title(f"winrate({lastTime})")
    plt.plot(x, y)
    plt.fill_between(x, y, color="skyblue", alpha=0.4)
    plt.ylim(0, 100)
    plt.xlabel("time")

    # 十字線
    ax = plt.gca()
    _ = Cursor(ax, useblit=True, color="blue", linewidth=1)

    plt.axhline(50, color="red")  # 50%線

    plt.show()


if __name__ == "__main__":
    main()
