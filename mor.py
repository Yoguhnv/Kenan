import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def draw_calculator():
    print(" _____________________")
    print("|  _________________  |")
    print("| |KENAN BABA TARAFINDAN | |")
    print("| |_________________| |")
    print("|  ___ ___ ___   ___  |")
    print("| | 7 | 8 | 9 | | + | |")
    print("| |___|___|___| |___| |")
    print("| | 4 | 5 | 6 | | - | |")
    print("| |___|___|___| |___| |")
    print("| | 1 | 2 | 3 | | x | |")
    print("| |___|___|___| |___| |")
    print("| | . | 0 | = | | / | |")
    print("| |___|___|___| |___| |")
    print("|_____________________|")

draw_calculator()

while True:
    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
    if operation == 'q':
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        continue
    print("Result: ", result)
  
