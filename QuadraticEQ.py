# Jack Dauenhauer 6/8/2022
# First try on own to create a simple program
# Goal: create a quadratic equation calculator

#import Math library
import math

# Get input from user
print("Enter the coefficients: A, B, & C")

A = int(input("Enter A:"))
B = int(input("Enter B:"))
C = int(input("Enter C:"))

print("You entered A = ",  A, " B = ", B, " C = ", C)

#Find the roots with the quadratic equation
X1 = ((-1 * B) + math.sqrt(B**2 - (4*A*C)))/(2*A)
X2 = ((-1 * B) - math.sqrt(B**2 - (4*A*C)))/(2*A)

print("The values of the roots are X1 = ", X1, "X2 = ", X2)