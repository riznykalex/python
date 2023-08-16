import os
import tkinter as tk
from tkinter import filedialog
import re

def create_empty_files():
    result_dir = result_dir_entry.get()

    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    def replace_invalid_chars(name):
        invalid_chars = r'[\\/:*?"<>|]'
        return re.sub(invalid_chars, "_", name)

    file_path = file_path_entry.get()

    with open(file_path, "r", encoding="utf-8") as file:
        file_names = file.read().splitlines()

    success_count = 0
    error_count = 0

    for file_name in file_names:
        modified_file_name = replace_invalid_chars(file_name)
        file_path = os.path.join(result_dir, modified_file_name)

        try:
            with open(file_path, "w", encoding="utf-8"):
                success_count += 1
        except Exception as e:
            error_count += 1

    result_label.config(text=f"Empty files created successfully: {success_count}\nErrors: {error_count}", font=("Helvetica", 12))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def choose_result_dir():
    result_dir = filedialog.askdirectory()
    result_dir_entry.delete(0, tk.END)
    result_dir_entry.insert(0, result_dir)

root = tk.Tk()
root.title("Файлики для Натусі")

file_label = tk.Label(root, text="Вибери текстовий файл з іменами файлів:", font=("Helvetica", 12))
file_label.pack()

file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack()

browse_button = tk.Button(root, text="Вибрати файл", command=browse_file)
browse_button.pack()

result_dir_label = tk.Label(root, text="Вибири папку для створення:", font=("Helvetica", 12))
result_dir_label.pack()

result_dir_entry = tk.Entry(root, width=50)
result_dir_entry.pack()

result_dir_button = tk.Button(root, text="Вибрати папку", command=choose_result_dir)
result_dir_button.pack()

create_button = tk.Button(root, text="Створити файли", command=create_empty_files)
create_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

root.mainloop()
