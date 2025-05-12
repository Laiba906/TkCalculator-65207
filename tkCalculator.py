# import tkinter as tk

# def add():
#     result.set(float(num1.get()) + float(num2.get()))

# def subtract():
#     result.set(float(num1.get()) - float(num2.get()))

# def multiply():
#     result.set(float(num1.get()) * float(num2.get()))

# def divide():
#     try:
#         result.set(float(num1.get()) / float(num2.get()))
#     except ZeroDivisionError:
#         result.set("Error")

# # GUI setup
# root = tk.Tk()
# root.title("Simple Calculator")

# num1 = tk.StringVar()
# num2 = tk.StringVar()
# result = tk.StringVar()

# tk.Label(root, text="Number 1").grid(row=0, column=0)
# tk.Entry(root, textvariable=num1).grid(row=0, column=1)

# tk.Label(root, text="Number 2").grid(row=1, column=0)
# tk.Entry(root, textvariable=num2).grid(row=1, column=1)

# tk.Button(root, text="Add", command=add).grid(row=2, column=0)
# tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
# tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
# tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)

# tk.Label(root, text="Result").grid(row=4, column=0)
# tk.Entry(root, textvariable=result, state="readonly").grid(row=4, column=1)

# root.mainloop()


import tkinter as tk
import math

# Global expression string
expression = ""

def update_input(value):
    global expression
    if value == "C":
        expression = ""
    elif value == "=":
        try:
            expr = expression.replace("x²", "**2").replace("√", "math.sqrt")
            result = eval(expr)
            expression = str(result)
        except:
            expression = "Error"
    else:
        expression += value
    input_var.set(expression)

# GUI Setup
root = tk.Tk()
root.title("Mobile Calculator")
root.geometry("350x500")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Input field
input_var = tk.StringVar()
entry = tk.Entry(root, textvariable=input_var, font=("Arial", 24), bd=0,
                 bg="#1e1e1e", fg="white", justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

# Frame for buttons
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both", padx=10, pady=10)

# Button styling
btn_font = ("Arial", 18)
btn_bg = "#333"
btn_fg = "white"
btn_active_bg = "#555"
btn_special_bg = "#fe9037"
btn_special_active = "#e67e22"

# Button layout
buttons = [
    ["C", "x²", "√", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Configure grid weights for resizing
for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# Create buttons
for r, row in enumerate(buttons):
    c = 0
    while c < len(row):
        btn_text = row[c]

        # Special case for '0' to span two columns
        if r == 4 and btn_text == "0":
            btn = tk.Button(frame, text=btn_text, font=btn_font,
                            bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                            bd=0, relief="ridge",
                            command=lambda txt=btn_text: update_input(txt))
            btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=5, pady=5)
            c += 2  # Skip next column
            continue

        # Special case for '=' button styling
        elif btn_text == "=":
            btn = tk.Button(frame, text=btn_text, font=btn_font,
                            bg=btn_special_bg, fg="white", activebackground=btn_special_active,
                            bd=0, relief="ridge",
                            command=lambda txt=btn_text: update_input(txt))
        else:
            btn = tk.Button(frame, text=btn_text, font=btn_font,
                            bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                            bd=0, relief="ridge",
                            command=lambda txt=btn_text: update_input(txt))

        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
        c += 1

root.mainloop()
