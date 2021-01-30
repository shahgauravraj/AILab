import math
import random
#-------------------------------------------------------------------------#
# Program to Print Hello world!
print("Hello, World!")

#-------------------------------------------------------------------------#

# Program to Add Two Numbers
def add(a, b):
    return a + b

print(add(2, 3))

#-------------------------------------------------------------------------#

# Program to Find the Square Root
def sq_root(a):
    return a ** 0.5

print(sq_root(25))

#-------------------------------------------------------------------------#

# Program to Calculate the Area of a Triangle
def area_of_triangle(a, b, c):
    if (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <= a) ):
        print('Not a valid triangle!') 
        return
          
    # calculate the semi-perimeter
    s = (a + b + c) / 2
      
    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('Area of a traingle is %f' %area)

#initialize the sides of triangle
a = 3.0
b = 4.0
c = 5.0

area_of_triangle(a,b,c)

#-------------------------------------------------------------------------#

# Program to Solve Quadratic Equation (Form: ax^2 + bx + c)

# function for finding roots
def quad_soln( a, b, c):

    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

    # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

# Driver Program
a = 1
b = -4
c = 6.25

# If a is 0, then incorrect equation
if a == 0:
        print("Input correct quadratic equation")

else:
    quad_soln(a, b, c)

#-------------------------------------------------------------------------#

# Program to Swap Two Variables

def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    print("a = {}  b = {}".format(a, b))

a = 10
b = 20

swap(a, b)

#-------------------------------------------------------------------------#

# Program to Generate a Random Number
print(random.randrange(1, 100))

#-------------------------------------------------------------------------#

# Program to Convert Kilometers to Miles
def kilo_to_miles(a):
    # since 1 km = 0.621371 miles
    return a * 0.621371

x = 100

print(kilo_to_miles(x))

#-------------------------------------------------------------------------#

# Program to Convert Celsius To Fahrenheit
def celsius_to_fehrenheit(a):
    return (a * 9/5) + 32

cel = 38
feh = celsius_to_fehrenheit(cel)

print("{} °C = {} °F".format(cel, feh))

#-------------------------------------------------------------------------#

# Program to sort numbers in ascending and descending order
Start = 1
Stop = 100
limit = 10

randnums = [random.randint(Start, Stop) for iter in range(limit)]

print("Numbers are: {}\n".format(randnums))

randnums.sort()

print("Numbers in ascending order:")
print(randnums)
print("\n")
randnums.sort(reverse=True)

print("Numbers in descending order:")
print(randnums)
print("\n")
