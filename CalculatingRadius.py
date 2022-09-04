# Calculating the area of a circle

# We first need to import the math module
import math

# Getting the radius of the circle

r = input(" What is the radius of your circle : ")
area = math.pi *math.pow(int(r), 2)
print(area)