def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error:Divided by zero."

def modulus(a, b):
    return a % b

print("Simple Calculator")

while True:
    print("\nSelect the arithmatic operation:")
    print("1. Addition '+'")
    print("2. Subtraction '-'")
    print("3. Multiplication '*'")
    print("4. Division '/'")
    print("5. Modulus/Remainder '%'")
    print("6. Exit")

    option = input("Enter the option between 1 to 6: ")

    if option in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option == '1':
            print("Result:", add(num1, num2))
        elif option == '2':
            print("Result:", subtract(num1, num2))
        elif option == '3':
            print("Result:", multiply(num1, num2))
        elif option == '4':
            print("Result:", divide(num1, num2))
        elif option == '5':
            print("Result:", modulus(num1, num2))
        elif option == '6':
            print("Exiting from the calculator.")
        break
    else:
        print("Invalid input. Please enter a valid input");