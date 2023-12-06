# Request numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

# Request action
action = str(input("Enter action: * or + : "))

# Сheck and output result
if action == "*":
    print(number1 * number2 * number3)
elif action == "+":
    print(number1 + number2 + number3)
else: 
    print("Repeat please")
    



