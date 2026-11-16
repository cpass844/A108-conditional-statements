#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"


num = float(input("What is your number?"))
r = num%2

if r==1:
    print("Your number is odd")
if r==0:
    print("Your number is even")

    