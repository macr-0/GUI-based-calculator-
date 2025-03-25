import tkinter as tk
from tkinter import messagebox
import math

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == '=':
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == 'C':
        entry_var.set("")
    elif button_text == '√':
        try:
            result = math.sqrt(float(current_text))
            entry_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == '^':
        entry_var.set(current_text + '**')
    else:
        entry_var.set(current_text + button_text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify='right')
entry.pack(fill='both', padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+'),
    ('√', '^')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    button_row = tk.Frame(frame)
    button_row.pack(side='top', expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(button_row, text=btn_text, font=("Arial", 14), command=lambda text=btn_text: on_click(text))
        btn.pack(side='left', expand=True, fill='both')

root.mainloop()
