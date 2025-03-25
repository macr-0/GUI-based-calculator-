operator = str(input("Enter your operator (* , / , +, -): "))

num1 = int(input("Enter your fist number: "))

num2 = int(input("enter your second number: "))

if operator == "*":
    print(num1 * num2)

elif operator == "+":
    print(num1 + num2)

elif operator == "/":
    print(num1 / num2)

else:
    print(num1 - num2)