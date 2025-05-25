# Python program to create a simple calculator

# Step 1: Functions for operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."

def average(num1, num2):
    return (num1 + num2) / 2

# Step 2: User input
print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Average")

select = int(input("Select an operation from 1, 2, 3, 4, 5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Step 3: Print the result
if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))
elif select == 2:
    print(number1, "-", number2, "=", subtract(number1, number2))
elif select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=", divide(number1, number2))
elif select == 5:
    print("Average of", number1, "and", number2, "=", average(number1, number2))
else:
    print("Invalid input")

