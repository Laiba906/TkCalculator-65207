import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    try:
        result.set(float(num1.get()) / float(num2.get()))
    except ZeroDivisionError:
        result.set("Error")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

tk.Label(root, text="Number 1").grid(row=0, column=0)
tk.Entry(root, textvariable=num1).grid(row=0, column=1)

tk.Label(root, text="Number 2").grid(row=1, column=0)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)

tk.Label(root, text="Result").grid(row=4, column=0)
tk.Entry(root, textvariable=result, state="readonly").grid(row=4, column=1)

root.mainloop()
