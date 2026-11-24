#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
print("Is this a right triangle? Enter your units!\n")

s1 = float(input("Enter one side:"))
s2 = float(input("Enter a second side:"))
s3 = float(input("Enter a third side:"))

import math 

hyp = float(max(s1, s2, s3))
c = hyp**2
sum = (s1**2)+(s2**2)+(s3**2)-c
if sum == c:
    print('that is a right triangle')
if sum > c: 
    print('that is an acute triangle')
if sum < c:
    print('that is an obtuse triangle')

