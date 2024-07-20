#1. Decisions at the Crossroad

#Task 1: Code Correction 
# You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. 
# Identify and fix them. 
#Buggy Code:

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")

#2. The Greatest Showdown

#Task 1: 
# Identify the Greatest 
# Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

#Task 2: 
# Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

#Expected Outcome: 
# If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "

enter_number = int(input("Either enter 3, 3, or 4: "))

if enter_number == 3:
    print("The smallest number is 3!")
elif enter_number == 4:
    print("The biggest number is 4!")
else:
    print(input("Follow instructions and please enter either 3 or 4: "))

#Second version of the code. The instructions are confusing, especially asking to write 3,3, and 4

enter_numberA = int(input("Guess! Enter a number 1 through 4: "))

if enter_numberA >= 4:
    print("The biggest number is 4!")
elif enter_numberA <= 4:
    print("The smallest number is 3!")
 

#3. Leap Year Explorer

#Task 1: Leap Year Checker
#Write a Python program that prompts the user to input a year.
#The program should determine if the given year is a leap year or not and then display an appropriate message.
 
#Please note that this is the definition of a leap year: 
#Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400.

#Expected Outcome: 
# If you test the year 1900, is should be False. 
# The year 2000 should be True. The year 2024 should be True



#I apologize. I got stuck really bad on this code. Please provide feedback so I can redo it. Thanks!