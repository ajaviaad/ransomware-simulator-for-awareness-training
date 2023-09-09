import os
import tkinter as tk
from tkinter import messagebox

TARGET_DIR = './dummy_data'
FAKE_EXTENSION = '.locked'


def fake_encrypt():
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            src = os.path.join(root, file)
            dst = src + FAKE_EXTENSION
            os.rename(src, dst)


def fake_decrypt():
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(FAKE_EXTENSION):
                src = os.path.join(root, file)
                dst = src.replace(FAKE_EXTENSION, '')
                os.rename(src, dst)


def display_ransom_note():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo(
        "RANSOMWARE SIMULATION",
        "Your files have been 'encrypted'! To 'decrypt' them, click OK. "
        "Remember, always be cautious with files from unknown sources!"
    )
    root.destroy()


def main():
    fake_encrypt()
    display_ransom_note()
    fake_decrypt()


if __name__ == "__main__":
    main()
