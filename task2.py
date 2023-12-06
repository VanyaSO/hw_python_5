# Request numbers
number1 = float(input("Enter number1 : "))
number2 = float(input("Enter number2 : "))
number3 = float(input("Enter numbe3 : "))

# Request action
action = input("Enter action: 1(max) or 2(min) or 3(aver)-arithmetic average : ") 

# We announce the result
result = number1

# Сheck the action and calculate the result
if action == "1":
    if result < number2:
        max = number2 
    elif result < number3:
        max = number3
elif action == "2":
    if result > number2:
        min = number2   
    elif result > number3:
        min = number3
elif action == "3":
    result = (number1 + number2 + number3) / 3
        
print(result)
        





