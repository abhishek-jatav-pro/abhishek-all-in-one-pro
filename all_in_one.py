# ABHISHEK ALL-IN-ONE PRO v5.1
# Made by Abhishek Jatav

print("=== ABHISHEK ALL-IN-ONE PRO ===")

while True:
    print("\n1. Calculator")
    print("2. Age Calculator")
    print("3. File Save Test")
    print("4. Exit")

    ch = input("Choice daalo (1-4): ")

    if ch == '1':
        a = int(input("Pehla number: "))
        b = int(input("Dusra number: "))
        print(f"Jod = {a+b}")
        with open("data.txt", "a") as f:
            f.write(f"Calc: {a}+{b}={a+b}\n")

    elif ch == '2':
        birth = int(input("Birth Year: "))
        print(f"Tumhari Age: {2026 - birth}")

    elif ch == '3':
        name = input("Apna naam likho: ")
        with open("data.txt", "a") as f:
            f.write(f"User: {name}\n")
        print("File me save ho gaya!")

    elif ch == '4':
        print("Bye Bhai! Project Khatam!")
        break
    else:
        print("Galat choice!")v
