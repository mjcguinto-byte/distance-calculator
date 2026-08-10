import math 

x1 = float(input("Enter x1: "))
y1 = float(input("Enter x2: "))
x2 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))
#Input the 4 values in order for the calculator to get the distance

d = math.sqrt((pow(x2-x1, 2) + pow(y2-y1, 2)))
print("The distance is", round(d, 2))
