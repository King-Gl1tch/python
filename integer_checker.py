"""This programe will cheak to see if the user entered a valid integer 
    in a specific range of values"""

#Use constantes for the low and high values
LOW = 1
HIGH = 10

# Ask the user to type in a number 
num = input("pleases enter a integer")

#Cheak to see if the number is valid
if num.lstrip("-").isnumeric():
    num = int(num)
    # cheak to see if the number is in correct range
    if num < LOW:
        print(f"{num}is lower then ")
    elif num > HIGH:
        print(f"{num}is grater then {HIGH}")
    else:     
        print(F"Your number is {num}")
else:
    print(f"{num} is not an integer")