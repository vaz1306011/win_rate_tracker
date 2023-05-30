import json
import tkinter as tk
from datetime import datetime
from tkinter import font


def main():
    with open("data.json", "r") as f:
        data = json.load(f)

    root = tk.Tk()
    root.title("勝率記錄")
    root.geometry("300x200+700+500")
    root.configure(bg="#444654")
    root.resizable(False, False)
    root.bind("<Escape>", lambda e: root.destroy())

    def write_result(win):
        time_ = time_box.get()
        if time_ not in data:
            data[time_] = []

        if win:
            data[time_]["win"] += 1
        else:
            data[time_]["lose"] += 1

        data["lastTime"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

        root.destroy()

    # 上面部分
    top_frame = tk.Frame(root, bg="#444654")
    top_frame.pack(pady=40)

    text_font = font.Font(size=20)
    # 勝利按鈕
    win_btn = tk.Button(
        top_frame,
        text="✅",
        command=lambda: write_result(True),
        font=text_font,
        bg="#343541",
        fg="#ffffff",
    )
    win_btn.pack(side="left", padx=20)

    # 失敗按鈕
    lose_btn = tk.Button(
        top_frame,
        text="❎",
        command=lambda: write_result(False),
        font=text_font,
        bg="#343541",
        fg="#ffffff",
    )
    lose_btn.pack(side="left", padx=20)

    # 下面部分
    bottom_frame = tk.Frame(root)
    bottom_frame.pack()

    text_font = font.Font(size=15)
    # 輸入框
    time_box = tk.Entry(
        bottom_frame, font=text_font, width=2, bg="#444654", fg="#ffffff"
    )
    now = datetime.now().strftime("%H")
    time_box.insert(0, now)
    time_box.pack(side="left")

    # 文字
    text = f"點,贏?"
    label = tk.Label(
        bottom_frame, text=text, font=text_font, bg="#444654", fg="#ffffff"
    )
    label.pack(side="left")

    root.mainloop()


if __name__ == "__main__":
    main()
