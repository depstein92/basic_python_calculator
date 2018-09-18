
#Python Calculator based on https://repl.it/@leoneloliver/Python-Calculator

def menu():
    print("__Welcome RoboCorp® Calculator__")
    print("1) Add")
    print("2) Subtract")
    print("3) Divide")
    print("4) Multiply")
    print("5) Quit")
    return input('Choose Input: ')

def add(num1, num2):
    total = num1 + num2
    print(num1 + num2)
    return total

def sub(num1, num2):
    total = num1 - num2
    print(num1 - num2)
    return total

def div(num1, num2):
    total = num1 / num2
    print(num1 / num2)
    return total

def mult(num1, num2):
    total = num1 ** num2
    print(num1 ** num2)
    return total

loop = 1
choice = 0
 while loop == 1:
     choice = menu()
     if choice == 1:
        add(input("Add this: ", input("to this: ")))
    elif choice == 2:
        sub(input("Subtract this: "), input("from this: "))
    elif choice == 3:
        div(input("Divide this: "), input("from this: "))
    elif choice == 4:
        mult(input("Multiply this: "), input("from this: "))
    elif choice == 5:
        print("thank you for using RoboCorp® Calulator")
        loop = 0;
