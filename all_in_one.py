# ABHISHEK ALL-IN-ONE SUPER PRO v6.0
# Made by Abhishek Jatav

import random
import datetime

print("=== ABHISHEK ALL-IN-ONE SUPER PRO v6.0 ===")

while True:
    print("\n1. Calculator")
    print("2. Age Calculator")
    print("3. Password Generator")
    print("4. To-Do List Save")
    print("5. Exit")

    ch = input("Choice (1-5): ")

    if ch == '1':
        a = int(input("Pehla number: "))
        b = int(input("Dusra number: "))
        print(f"Jod: {a+b} | Guna: {a*b}")
        with open("data.txt", "a") as f:
            f.write(f"Calc: {a},{b}\n")

    elif ch == '2':
        birth = int(input("Birth Year: "))
        print(f"Age: {2026 - birth} saal")

    elif ch == '3':
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$"
        length = int(input("Password length?: "))
        pwd = "".join(random.choice(chars) for _ in range(length))
        print(f"Password: {pwd}")

    elif ch == '4':
        task = input("Kaam likho: ")
        with open("data.txt", "a") as f:
            f.write(f"TODO: {task}\n")
        print("Save Ho Gaya!")

    elif ch == '5':
        print("Bye! v6.0 Khatam!")
        break
