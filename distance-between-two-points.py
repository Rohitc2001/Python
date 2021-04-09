                    # Program to find distance between two points.
import math

x1 = int(input("Enter Point-1 x-coordinate : "))
y1 = int(input("Enter Point-1 y-coordinate : "))
x2 = int(input("Enter Point-2 x-coordinate : "))
y2 = int(input("Enter Point-2 y-coordinate : "))

distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print("Distance between two points is : ",distance)
