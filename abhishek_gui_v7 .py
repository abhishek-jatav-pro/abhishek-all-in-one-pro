import tkinter as tk
from tkinter import messagebox
import random
import string

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = op_var.get()
        if op == "+": res = a+b
        elif op == "-": res = a-b
        elif op == "*": res = a*b
        elif op == "/": res = a/b if b!=0 else "Error"
        result_label.config(text=f"Result: {res}")
    except:
        messagebox.showerror("Error","Sahi number daal bhai!")

def generate_pass():
    chars = string.ascii_letters + string.digits + "!@#$%"
    pwd = "".join(random.choice(chars) for _ in range(12))
    result_label.config(text=f"Password: {pwd}")

def check_age():
    try:
        age = int(entry1.get())
        if age >= 18: msg = "Tu Adult hai Bhai!"
        else: msg = f"Tu {18-age} saal baad Adult banega!"
        result_label.config(text=msg)
    except:
        messagebox.showerror("Error","Age daal!")

# Window
root = tk.Tk()
root.title("ABHISHEK ALL-IN-ONE PRO v7.0 - GUI")
root.geometry("400x450")
root.config(bg="#1a1a2e")

tk.Label(root, text="ABHISHEK PRO v7.0", font=("Arial",20,"bold"), bg="#1a1a2e", fg="#00ffcc").pack(pady=10)
tk.Label(root, text="Made by Abhishek Jatav", bg="#1a1a2e", fg="white").pack()

entry1 = tk.Entry(root, font=("Arial",14)); entry1.pack(pady=5); entry1.insert(0,"Pehla Number / Age")
entry2 = tk.Entry(root, font=("Arial",14)); entry2.pack(pady=5); entry2.insert(0,"Dusra Number")

op_var = tk.StringVar(value="+")
tk.OptionMenu(root, op_var, "+","-","*","/").pack()

tk.Button(root, text="CALCULATE", command=calculate, bg="#00ffcc", font=("Arial",12,"bold"), width=20).pack(pady=5)
tk.Button(root, text="PASSWORD GENERATOR", command=generate_pass, bg="#ff006e", fg="white", font=("Arial",12,"bold"), width=20).pack(pady=5)
tk.Button(root, text="AGE CHECKER", command=check_age, bg="#ffbe0b", font=("Arial",12,"bold"), width=20).pack(pady=5)

result_label = tk.Label(root, text="Result Yahan Ayega", font=("Arial",14,"bold"), bg="#1a1a2e", fg="white", wraplength=350)
result_label.pack(pady=20)

root.mainloop()
