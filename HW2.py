# Task 1: Code Correction

#Version 1
number = int(input("Enter a number: "))

if number > 0:
   print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
else:
    print("Incorrect data type")

#Version 2
number = int(input("Enter a number: "))

if number > 0:
   print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    number < 0
    print("The number is negative.")

# Task 2: The Greatest Showdown

x = 3, 3, 4
y = "The smallest number is "
z = "The biggest number is "
print(y + str(min(x)))
print(z + str(max(x)))


#Task 3: Leap Year Explorer

user_input = int(input("Please enter a year (yyyy format): "))
if (user_input % 4 == 0 and user_input % 100 != 0) or user_input % 400 == 0:
     print(f"{bool(user_input)}: This is a leap year")
else:
     print("False - This is not a leap year")
