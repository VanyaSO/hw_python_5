# Request number of meters
number_meters = float(input("Enter the number of meters: "))

# Ask what to convert into
convert_to = input("Convert to 1(miles) 2(inches) or 3(yards)")

# Сheck and convet 
if convert_to == "1":
    print(f"{number_meters} in miles = {number_meters / 1609.34}miles")
elif convert_to == "2":
    print(f"{number_meters} in inches = {number_meters * 39.37}inches")
elif convert_to == "3":
    print(f"{number_meters} in yards = {number_meters * 1.094}yards")
