num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (+ or -): ")

addition = num1 + num2
subtraction = num1 - num2

if operator == "+":
    print("The sum of these numbers is " + str(addition))
elif operator == "-":
    print(num1, "minus", num2, "is", subtraction)
else:
    print("Invalid operator. Please enter + or -.")
