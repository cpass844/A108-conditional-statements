#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

num = float(input("What is your number?"))

r = num%1

if r==1 or 0 or -1:
    print("The number is an integer")
else:
    print("The number is NOT an integer!")
