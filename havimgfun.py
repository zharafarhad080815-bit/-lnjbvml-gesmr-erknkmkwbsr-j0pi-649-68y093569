text=str(input("enter a string: "))
print("the string is: ",text)
print("the length of the string is: ",len(text))
print("the string in uppercase is: ",text.upper())
print("the string in lowercase is: ",text.lower())
reversed_text=text[::-1]
print("the reversed string is: ",reversed_text)
text+=" World"
print("the updated string is: ",text)
print("the string starts with 'Hello': ",text.startswith("Hello"))
print("the string ends with 'World': ",text.endswith("World"))
print("the string contains 'lo Wo': ", "lo Wo" in text)
# --- IGNORE ---
print("the string after replacing 'Hello' with 'Hi': ",text.replace("Hello","Hi"))
print("the string after removing spaces: ",text.replace(" ",""))
#operation
A=10
B=5
C=A+B
print("The sum of A and B is: ",C)
D=A-B
print("The difference of A and B is: ",D)
E=A*B
print("The product of A and B is: ",E)
F=A/B
print("The quotient of A and B is: ",F)
g=A%B
print("The remainder of A divided by B is: ",g)
if A > B:
    print("A is greater than B")
elif A < B:
    print("A is smaller than B")
else:
    print("A is equal to B")
sunrise_time = "6:00 AM"
sunset_time = "6:00 PM"
print("The sunrise time is: ", sunrise_time)
print("The sunset time is: ", sunset_time)
sunny=input("Is it sunny today? (yes/no): ")
temperature=int(input("Enter the temperature in degrees Celsius: "))
if sunny.lower() == "yes" and temperature > 25:
    print("It's a great day to go outside and enjoy the sunshine.")
elif sunny.lower() == "no" and temperature < 20:
    print("It's a good day to stay indoors and read a book.")
else:
    print("It's a moderate day. You can do either activity.")
ch=input("Enter a character: ")
if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The character is a letter.")
else:
    print("The character is not a letter.")
    if ch.isdigit():
        print("The character is a digit.")
    else:
        print("The character is a special character.")
character=input("Enter a character: ")
anime=input("Enter your favorite anime: ")
print(f"The character {character} is from the anime {anime}.")

a=int (input("enter a number for a: "))
b=int (input("enter a number for b: "))
c=int (input("enter a number for c: "))
if a > b and a > c:
    print("a is the greatest number")
elif b > a and b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")

x=int (input("Enter a number for x: "))
y=int (input("Enter a number for y: "))
z=int (input("Enter a number for z: "))
B=int (input("Enter a number for B: "))
result = x + y * z / B
print("The result is:", result)
name=input("Enter your name: ")
age=int (input("Enter your age: "))
print("Hello,", name, "you are", age, "years old.")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the distance in kilometers: "))
total_time = a + b + c
average_speed = d / total_time
print("The average speed is:", average_speed, "km/h")
if average_speed > 60:
    print("The average speed is above the speed limit.")
else:
    print("The average speed is within the speed limit.")
#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
print("Welcome to Ride is Fun!")
print("Please select a category:")
print("1. Bike")
print("2. Car")
category = int(input("Enter your choice (1 or 2): "))
if category == 1:
    print("You selected Bike. Please select a type:")
    print("1. Mountain Bike")
    print("2. Road Bike")
    bike_type = int(input("Enter your choice (1 or 2): "))
    if bike_type == 1:
        print("You selected Mountain Bike.")
    elif bike_type == 2:
        print("You selected Road Bike.")
    else:
        print("Invalid choice for bike type.")
elif category == 2:
    print("You selected Car. Please select a type:")
    print("1. Sedan")
    print("2. SUV")
    car_type = int(input("Enter your choice (1 or 2): "))
    if car_type == 1:
        print("You selected Sedan.")
    elif car_type == 2:
        print("You selected SUV.")
    else:
        print("Invalid choice for car type.")
else:
    print("Invalid choice for category.")
#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
marrdic = input("Do you have a medical cause? (Y/N): ")
if marrdic == 'Y': 
    print("You are allowed to take the exam.")
else:
    attendance = float(input("What is your attendance percentage? "))
    if attendance > 75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam.")
#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
units = float(input("Enter the number of units consumed: ")) 
if units < 50:
    cost_per_unit = 2.60
    tax = 25
elif 50 <= units < 100:
    cost_per_unit = 3.25
    tax = 35
elif 100 <= units < 200:
    cost_per_unit = 5.26
    tax = 45
else:
    cost_per_unit = 8.45
    tax = 75
bill_amount = (units * cost_per_unit) + tax
print(f"Your electricity bill is: {bill_amount:.2f}")
#Write a program to check the age entered by the user is between 10 to 20 years or not?
age = int(input("Enter your age: "))
if 10 <= age <= 20:
    print("Your age is between 10 and 20.")
else:
    print("Your age is not between 10 and 20.")
n=int(input("enter a number:"))
for i in range(n,0,-1):
    print(i)
n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
S=input("enter a word")
s2=""
for i in S:
    s2 =i + s2
print(s2)
base=int(input("enter the base"))
exp=int (input("enter exp"))
result=1
for i in range(exp):
    result=result *base
print(result)
N= int(input("enter an number"))
sum=0
i=1
while i<=N:
    sum=sum+i
    i=i+1
print("the sum of first",N,"natural numbers is",sum)
i=0
while i<=0:
    print("Hello, World!")
    break
# Check if a number is an Armstrong number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
    # how many total digits are in a number entered by the user?
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("The total number of digits in the entered number is:", count)
# What is the product of the middle digits of a number?
num = int(input("Enter a number: "))
num_str = str(num)
length = len(num_str)
if length % 2 == 1:
    middle_index = length // 2
    product = int(num_str[middle_index])
else:
    middle_index1 = length // 2 - 1
    middle_index2 = length // 2
    product = int(num_str[middle_index1]) * int(num_str[middle_index2])
print(f"The product of the middle digits of {num} is {product}.")
# Is this a Prime Number?
lower=int(input("Enter a number: "))
higher=int(input("Enter another number: "))
for num in range(lower, higher + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, "is a prime number")
 # how many times a character is repeated in a word?
word = input("Enter a word: ")
character = input("Enter a character to count: ")
i=0
count = 0 
while i < len(word):
    if word[i] == character:
        count += 1
    i += 1
print(f"The character '{character}' appears {count} times in the word '{word}'.")
#decimal number into a binary number?
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # Remove the '0b' prefix
print(f"The binary representation of {decimal} is {binary}.")
# demonstrate a right angle triangle pattern?
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
    # demonstrate Floyd's triangle pattern?
n = int(input("Enter the number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
    # demonstrate a diamond pattern?
n = int(input("Enter the number of rows for the upper half: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    # demonstrate a mirrored triangle pattern?
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    # what is the sum of the first n natural numbers?
n=int(input("enter a number"))
sum=0 
for i in range(1,n+1):
    sum=sum+i
print(sum)
# what are keywords in Python?
import keyword
print("The keywords in Python are:")
print(keyword.kwlist)
# what are the built-in functions in Python?
import builtins
print("The built-in functions in Python are:")
print(dir(builtins))
# what are the data types in Python?
print("The data types in Python include:")
print(type(5))  # <class 'int'>
print(type(5.0))  # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({1, 2, 3}))  # <class 'set'>
print(type({1: "one", 2: "two"}))  # <class 'dict'>
# what are the operators in Python?
print("The operators in Python include:")
print("Arithmetic operators: +, -, *, /, %, **, //")
print("Comparison operators: ==, !=, >, <, >=, <=")
print("Logical operators: and, or, not")
print("Bitwise operators: &, |, ^, ~, <<, >>")
#what are the control flow statements in Python?
print("The control flow statements in Python include:")
print("Conditional statements: if, elif, else")
print("Looping statements: for, while")
print("Control statements: break, continue, pass")
# is Python case-sensitive?
print("Yes, Python is case-sensitive. For example:")
print("Variable 'x' and 'X' are different in Python.")
# how to comment in Python?
print("In Python, you can use the '#' symbol to add a comment. For example:")
print("# This is a comment in Python")
import turtle


turtle.Screen().bgcolor("lightblue")
turtle.color("red")
turtle.Screen ().setup(400,400)
pen=turtle.Turtle()
sides=int(input("Enter the number of sides: "))
angle=360/sides
for i in range(sides):
    pen.forward(100)
    pen.left(angle)
turtle.done()
import turtle

turtle.Screen().bgcolor("purple")
turtle.color("pink")
turtle.Screen ().setup(400,400)
pen=turtle.Turtle()
sides=5
angle=144
for i in range(sides):
    pen.forward(100)
    pen.left(angle)
turtle.done()
import turtle

turtle.Screen().bgcolor("lightblue")
turtle.color("red")
turtle.Screen().setup(400, 400)
pen = turtle.Turtle()
pen.speed(5)

# Draw a spiral pattern
for i in range(70):
    pen.forward(i * 5)
    pen.right(90)
turtle.done()
import turtle

turtle.Screen().bgcolor("lightblue") 
turtle.color("red")
turtle.Screen().setup(400, 400)
pen = turtle.Turtle()
for i in range(4):
    pen.forward(100)
    pen.left(90)
turtle.done()
import turtle

turtle.Screen().bgcolor("lightblue")
turtle.color("red")
turtle.Screen().setup(400, 400)
pen = turtle.Turtle()
for i in range(3):
    pen.forward(100)
    pen.left(90)
turtle.done()
def well_wishes():
    print("Wishing you all the best in your endeavors!")
    print("May your dreams come true and your efforts be rewarded.")
    print("Stay positive and keep striving for greatness!")
    print("Remember, every step forward is a step towards success.")
    print("Good luck and may you achieve everything you desire!")
well_wishes()
def weather_condition():
    print("The weather today is sunny with a high of 25 degrees Celsius.")
    print("There is a light breeze coming from the northwest.")
    print("Humidity levels are at 60%, making it feel comfortable outside.")
    print("No precipitation is expected, so it's a great day to be outdoors!")
    print("Remember to stay hydrated and wear sunscreen if you're spending time in the sun.")
weather_condition()
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference
radius = float(input("Enter the radius of the circle: "))
result = calculate_circumference(radius)
print(f"The circumference of the circle is: {result:.2f}")
 #Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
def total_calc(bill_amount, tip_perc):
    tip_amount = bill_amount * (tip_perc / 100)
    total_amount = bill_amount + tip_amount
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip Percentage: {tip_perc}%")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Amount to Pay: ${total_amount:.2f}")
#Example usage:
total_calc(50, 15)
#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(num):
    return num ** 3

def cube_if_divisible_by_3(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return None
#Example usage:
number = 9
result = cube_if_divisible_by_3(number)
if result is not None:
    print(f"The cube of {number} is {result}")
else:
    print(f"{number} is not divisible by 3, so no cube is calculated.")
    #Write a program to find the factorial using recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
#Write a program to define the shutdown function. The function should print "Shutting down the system..." when called. Then, call the shutdown function to see the output.
def shutdown():
    print("Shutting down the system...")
# Call the shutdown function
shutdown()
word= input("Enter a word: ") 
for letter in word:
    if letter == "a":
        print("The letter 'a' was found in the word.")
        break
    else:
        print(f"The letter '{letter}' is not 'a'.")
print("Finished searching for the letter 'a'.")
    #If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.
for i in range(1,20):
    if i % 20 == 0:
        print("twist")
    elif i % 15 == 0:
        pass
    elif i % 5 == 0:
        print("fizz")
    elif i % 3 == 0:
        print("buzz")
    else:
        print(i)
        #display 1 to 10 numbers in reverse order and skip the number 5.
for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)
    # calculate the customer due amount after paying a bill of a certain amount
bill_amount = float(input("Enter the bill amount: "))
payment_amount = float(input("Enter the payment amount: "))
due_amount = bill_amount - payment_amount
print(f"The customer is due to pay: ${due_amount:.2f}")
if due_amount > 0:
    print("The customer still owes money.")
elif due_amount < 0:
    print("The customer has overpaid.")
else:
    print("The customer has paid the exact amount.")
try:
    N=int(input("Enter a number: "))
    print("You entered:", N)
except ValueError as e:
    print("Invalid input. Please enter a valid integer.")
    print("Error details:", e)
try:
    a,b= eval(input("Enter two numbers separated by a comma: "))
    result = a / b
    print("The result of the division is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Error: Please enter the numbers in the correct format (separated by a comma).")
except Exception as e:
    print("An unexpected error occurred:", e)  
else:
    print("Division performed successfully.")
finally:
    print("This block will always execute, regardless of exceptions.")
# If the value is divided by two, then it will run an infinite loop of the bye.
valid = False
while not valid:
    try:
        N = int(input("Enter a number: "))
        valid = True
        while N % 2 == 0:
            print("Bye")
            break
        valid = True 
    except ValueError as e:
        print("Invalid input. Please enter a valid integer.")
        print("Error details:", e)
#check the age entered by the user is correct or not. If there is some error in the value of age entered. And check that the age entered by the user is even or odd.
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError as e:
    print("Invalid input. Please enter a valid age.")
    print("Error details:", e)
# write a progrom to know what are prime numbers between 1 to 100 and handle the exception if the user enters a non-integer value.
try:
    lower=int(input("Enter a number: "))
    higher=int(input("Enter another number: "))
    for num in range(lower, higher + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, "is a prime number")
except ValueError as e:
    print("Invalid input. Please enter valid integers.")
    print("Error details:", e)
    import random
playing = True
number = random.randint(0,9)
while playing:    
    guess = int(input("Guess a number between 0 and 9: "))
    if guess == number:
        print("Congratulations! You guessed the number.")
        playing = False
    else:
        print("Wrong guess. Try again!")
        import random
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
import math
print("Square root of 16 is:", math.sqrt(16))
print("Factorial of 5 is:", math.factorial(5))
print ( "gcd of 48 and 18 is:", math.gcd(48, 18))
print ("LCM of 4 and 6 is:", math.lcm(4, 6))
print (" copy sign of -5 is:", math.copysign(1, -5))
print ("ceil of 3.7 is:", math.ceil(3.7))
print ("floor of 3.7 is:", math.floor(3.7))
#calculate the values of sin, cos, and tan using the math module.
import math
angle = float(input("Enter an angle in degrees: "))
angle_rad = math.radians(angle)
print("sin({}°) = {}".format(angle, math.sin(angle_rad)))
print("cos({}°) = {}".format(angle, math.cos(angle_rad)))
print("tan({}°) = {}".format(angle, math.tan(angle_rad)))
# List of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
for month in months:
    print(month)
    #1.  4 functions defined — add, subtract, multiply, divide

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
#2.  User input for operation and numbers
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input. Please enter a valid operation.")
def word_matching(list1):
    count = 0
    list2 = []
    for i in list1:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
            list2.append(i)
    return count, list2
# Example usage
input_list = ['abc', 'xyz', 'aba', '1221']
count, matched_words = word_matching(input_list)
print("Count:", count)
print("Matched Words:", matched_words)
#Write a program to perform the following operations on a List: 1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list
#1. Create an empty list
empty_list = []

#2. A list with elements
elements_list = [1, 2, 3, 4, 5]

#3. Use * operator
multiplied_list = elements_list * 2

#4. Reverse a list
reversed_list = elements_list[::-1]
print("Empty List:", empty_list)
print("List with Elements:", elements_list)
print("Multiplied List:", multiplied_list)
print("Reversed List:", reversed_list)
#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
# Function to calculate sum, average, largest and smallest
list_numbers = [10, 20, 30, 40, 50]
total_sum = sum(list_numbers)
average = total_sum / len(list_numbers)
largest = max(list_numbers)
smallest = min(list_numbers)
print("Sum:", total_sum)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)
list=[5,25,12,8,15]
list.sort()
print("Sorted List:", list)
#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
#1. Create a tuple with different datatypes
my_tuple = (1, "Hello", 3.14, True)

#2. Create another tuple of integers
int_tuple = (10, 20, 30, 40, 50)

#3. Create a new tuple by adding 9 to the previous tuple
new_tuple = int_tuple + (9,)

#4. Count the occurrences of an element in the tuple
count = my_tuple.count("Hello")

#5. Perform slicing on the tuple
sliced_tuple = my_tuple[1:3]
print("Original tuple:", my_tuple)
print("Integer tuple:", int_tuple)
print("New tuple:", new_tuple)
print("Count of 'Hello':", count)
print("Sliced tuple:", sliced_tuple)
#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
my_tuple = (1, 2, 3, 3, 2, 1)
reversed_tuple = my_tuple[::-1]
if my_tuple == reversed_tuple:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")
#Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.
weather = (1, 0, 0, 0, 1, 1, 0)
rainy = 0
sunny = 0

for element in weather:
    if element == 1:
        rainy += 1
    else:
        sunny += 1

if rainy > sunny:
    print("It is likely to rain.")
elif sunny > rainy:
    print("It is likely to be sunny.")
else:
    print("The weather is uncertain.")
#Write a Python program to calculate the product, multiplying all the numbers of the given tuple.
my_tuple = (2, 3, 4, 5)
product = 1
for num in my_tuple:
    product *= num
print("Product:", product)
dictionary = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
value_to_check = 2
result = 0
for value in dictionary.values():
    if value == value_to_check:
        result += 1
print(f"The frequency of {value_to_check} is: {result}")
#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
dictionary = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
value_to_check = 2
result = 0
for value in dictionary.values():
    if value == value_to_check:
        result += 1
print(f"The frequency of {value_to_check} is: {result}")
student_details = {
    "id1": {"name": "Alice", "age": 20},
    "id2": {"name": "Bob", "age": 22},
    "id3": {"name": "Alice", "age": 20},
    "id4": {"name": "Charlie", "age": 23},
    "id5": {"name": "Bob", "age": 22},
    "id6": {"name": "David", "age": 21},
    "id7": {"name": "Eve", "age": 24}
}
unique_students = {}
unique_key=[]
for key, value in student_details.items():
    if value not in unique_students.values():
        unique_students[key] = value
        unique_key.append(key)
for k, v in unique_students.items():
    print(f"{k}: {v}")
    #Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
country_codes = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print(country_codes.get('India', 'Country not found'))
print(country_codes.get('Australia', 'Country not found'))
print(country_codes.get('Nepal', 'Country not found'))
print(country_codes.get('Bangladesh', 'Country not found'))
#Write a program to check if a key exists in a dictionary. If the key exists, print the value associated with that key; otherwise, print "Key not found."
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key_to_check = input("Enter a key to check: ")
if key_to_check in my_dict:
    print(f"The value associated with '{key_to_check}' is: {my_dict[key_to_check]}")
else:
    print("Key not found.")
#Write a program to find the sum of all the values in a dictionary. The dictionary is - {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
total_sum = sum(my_dict.values())
print("The sum of all the values in the dictionary is:", total_sum)
if key_to_check in my_dict:
    print(f"The value associated with '{key_to_check}' is: {my_dict[key_to_check]}")
    print("Key not found.")
else:
    print("Invalid input. Please enter a valid operation.")
#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
#1. Create a set with integer elements
integer_set = {1, 2, 3, 4, 5}
print("Set with integer elements:", integer_set)
#2. Create a set with mixed data type elements
mixed_set = {1, "Hello", 3.14, True}
print("Set with mixed data type elements:", mixed_set)
#3. Create another set with elements - 1, 2, 3, 4, 3, 2
another_set = {1, 2, 3, 4, 3, 2}
print("Set with duplicate elements (duplicates will be removed):", another_set)
#4. Create a set from a list with elements - [1, 2, 3, 2]
list_set = set([1, 2, 3, 2])
print("Set created from a list:", list_set)
#5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
# Note: Sets are unordered collections, so we cannot directly remove the "first" element.
# Instead, we will remove an arbitrary element using the pop() method.
if list_set:
    removed_element = list_set.pop()
    print(f"Set after removing an arbitrary element ({removed_element}):", list_set)
#Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}
# Define the two sets
set1 = {"green", "blue"}
set2 = {"blue", "yellow"}

# Find the intersection
intersection = set1 & set2
print("Intersection of the two sets:", intersection)
set3=set1.intersection(set2)
print("Intersection of the two sets using method:", set3)
#Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.
# Create the array
import array
arr = array.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array:", arr)
# Find the number of occurrences of number 3
count = arr.count(3)
print("Number of occurrences of 3:", count)
# Print the reversed array
print("Reversed array:", arr[::-1])
#Write a Python program to find the symmetric difference between two sets.
# Define the two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Find the symmetric difference
symmetric_difference = set1 ^ set2
print("Symmetric difference of the two sets:", symmetric_difference)
set3=set1.symmetric_difference(set2)
print("Symmetric difference of the two sets using method:", set3)
#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [1, 2, 3, 4]

# Adding numbers of two different lists
result1 = list(map(lambda x, y: x + y, list1, list2))
print("Addition of two lists:", result1)

# Squaring numbers of another list
result2 = list(map(lambda x: x ** 2, list3))
print("Square of numbers in the third list:", result2)
#Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# 1. zipped list from two lists
zipped_list = list(zip(list1, list2))
print("Zipped list from two lists:", zipped_list)

# 2. elements of two lists zipped together, but 2nd list in reverse order
zipped_reverse = list(zip(list1, reversed(list2)))
print("Zipped elements with second list in reverse order:", zipped_reverse)

# 3. elements of two lists zipped into a dictionary
zipped_dict = dict(zip(list1, list2))
print("Zipped elements into a dictionary:", zipped_dict)
#Write a program where the value of i begins from 1 and goes to 10. When the value of i becomes 5, force the interpreter to exit the program.
for i in range(1, 11):
    print(i)
    if i == 5:
        break
print("Program exited at i =", i)
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
result = [x + y for x, y in zip(num1, num2)]
print("Addition of two lists:", result)
squared_list = [x ** 2 for x in num1]
print("Square of numbers in the first list:", squared_list)
print("Zipped list from two lists:", list(zip(num1, num2)))
print("Zipped elements with second list in reverse order:", list(zip(num1, reversed(num2))))
print("Zipped elements into a dictionary:", dict(zip(num1, num2)))
num3 = [1, 2, 3, 4, 5]
print("Original list:", num3)
print("Reversed list:", num3[::-1])
num4 = [1, 2, 3, 4, 5]
print("Original list:", num4)
print("Reversed list:", num4[::-1])
num5 = [1, 2, 3, 4, 5]
print("Original list:", num5)
print("Reversed list:", num5[::-1])
num6 = [1, 2, 3, 4, 5]
print("Original list:", num6)
print("Reversed list:", num6[::-1])
num7 = [1, 2, 3, 4, 5]
print("Original list:", num7)
print("Reversed list:", num7[::-1])
num8 = [1, 2, 3, 4, 5]
print("Original list:", num8)
print("Reversed list:", num8[::-1])
print("Original list:", num8)
print("Reversed list:", num8[::-1])
num9 = [1, 2, 3, 4, 5]
print("Original list:", num9)
print("Reversed list:", num9[::-1])
num9 = [1, 2, 3, 4, 5]
print("Original list:", num9)
print("Reversed list:", num9[::-1])
num10 = [1, 2, 3, 4, 5]
print("Original list:", num10)
print("Reversed list:", num10[::-1])
#Write a program to find the sum of all the numbers in a list using a while loop.
numbers = [1, 2, 3, 4, 5]
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1
print("Sum of all numbers in the list:", total)
print("Hello, World!")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
#num = int(input("Enter a number: "))
try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
#Write a letter pattern program to print the following pattern:
# A
# B B
# C C C
# D D D D
# E E E E E
for i in range(1, 6):
    print(" ".join([chr(64 + i)] * i))
#Write a program to print the following pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1, 6):
    print(" ".join([str(i)] * i))
print("Hello, World!") 
print("Welcome to Python programming!")
print("Let's learn and have fun coding!")
print("Python is a versatile language.")
print("Happy coding!") 
# Happy coding!
print("Happy coding!")
input("Press Enter to continue...")
print("Thank you for using the program. Goodbye!")
# Continue with the program...
print("This is the next part of the program.")
input("Press Enter to continue...")
print("Continuing...")
print("This is the final part of the program. Goodbye!")
# End of the program
#Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.
# Dictionary created with at least 5 student name-score pairs  
grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96,
    "Eve": 88
}
#  A loop correctly calculates and prints the class average  
total = 0
for score in grade_book.values():
    total += score
average = total / len(grade_book)
print(f"Class average: {average}")
#  Highest and lowest scores and students identified    
max_score = max(grade_book.values())
min_score = min(grade_book.values())
top_student = [name for name, score in grade_book.items() if score == max_score]
bottom_student = [name for name, score in grade_book.items() if score == min_score]
print(f"Top scorer(s): {top_student} with a score of {max_score}")
print(f"Bottom scorer(s): {bottom_student} with a score of {min_score}")
#get() used to look up student — friendly message if missing 
student_name = input("Enter a student's name to look up their grade: ")
grade = grade_book.get(student_name, "Student not found.")
print(f"{student_name}'s grade is: {grade}")
# Program runs without any errors     
print("Program completed successfully.")
#Write a Python program to generate a random password consisting of lower case and upper case characters along with numbers. You can also use random module for shuffling the password generated.
import random

def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''.join(random.choice(characters) for _ in range(length))
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

print(generate_password())
#Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output
class Student:
    grade=5
    print(f"The student is in grade {grade}")
obj=Student()
#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = Vehicle(200, 50)
print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)
#Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well
class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

parrot1 = Parrot("Alice", 2)
parrot2 = Parrot("Bob", 3)

print("Species:", Parrot.species)
print("Name:", parrot1.name, "Age:", parrot1.age)
print("Name:", parrot2.name, "Age:", parrot2.age)
#Write a program to create a cat class with one class variable and two instance variables, and display the details of cat of two different breeds.
class Cat:
    species = "Mammal"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

cat1 = Cat("Fluffy", "Persian")
cat2 = Cat("Whiskers", "Siamese")

print("Species:", Cat.species)
print("Name:", cat1.name, "Breed:", cat1.breed)
print("Name:", cat2.name, "Breed:", cat2.breed)
#Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IOString:
    def __init__(self, str1=""):
        self.str1 = str1

    def get_string(self):
        self.str1 = input("Enter a string: ")

    def print_upper(self):
        print(self.str1.upper())

# Create an object and call methods
obj = IOString()
obj.get_string()
obj.print_upper()
#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(f"Employee {self.name} created with ID {self.id}")

    def __del__(self):
        print(f"Employee {self.name} with ID {self.id} deleted")

def create_and_delete_employee():
    emp = Employee("Alice", 123)
    del emp

create_and_delete_employee()
#Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)
class PairFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_pair(self, target_sum):
        num_dict = {}
        for i, num in enumerate(self.numbers):
            complement = target_sum - num
            if complement in num_dict:
                return (num_dict[complement], i)
            num_dict[num] = i
        return None

# Example usage
numbers = (10, 20, 30, 40, 50, 60, 70)
finder = PairFinder(numbers)
target_sum = int(input("Enter the target sum: "))
result = finder.find_pair(target_sum)
if result:
    print(f"Pair found at positions {result[0]} and {result[1]}")
else:
    print("No pair found")
    #Write a Python program to create a class named Circle constructed by a radius and two methods to compute the area and the perimeter of a circle.


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
#Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

# Create an instance of the Bus class
school_bus = Bus("School Volvo", 180, 12)

# Display the details of the bus
print(f"Name: {school_bus.name}, Max Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")
#Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(f"Name: {self.name}, ID Number: {self.id_number}")

class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post

    def display(self):
        super().display()
        print(f"Salary: {self.salary}, Post: {self.post}")

# Create an object for the child class and call the display method
emp = Employee("Alice", 12345, 50000, "Manager")
emp.display()
#Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.
class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def fly(self):
        print(f"{self.name} is flying.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")

class Penguin(Bird):
    def __init__(self, name, species, habitat):
        super().__init__(name, species)
        self.habitat = habitat

    def swim(self):
        print(f"{self.name} is swimming in {self.habitat}.")

    def make_sound(self):
        print(f"{self.name} is making a penguin sound.")

# Create an object for the child class and call the methods
penguin = Penguin("Pingu", "Emperor Penguin", "Antarctica")
penguin.fly()
penguin.swim()
penguin.make_sound()
#Create a Bus child class inherited from the Vehicle class to calculate the total fare.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def calculate_fare(self):
        return self.capacity * 100

# Create an instance of the Bus class
school_bus = Bus("School Volvo", 180, 12, 50)

# Calculate and display the total fare
print(f"Total fare for {school_bus.name}: ${school_bus.calculate_fare()}")
#Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
class MyClass:
    def __init__(self, value):
        self.__privateVar = value  # Private variable

    def __privMeth(self):  # Private method
        print("This is a private method.")

    def hello(self):  # Public method
        print(f"The value of privateVar is: {self.__privateVar}")
        self.__privMeth()  # Calling the private method from within the class

# Creating an object of the class
obj = MyClass(10)
obj.hello()  # Calling the public method
obj.__privMeth()  # This will raise an AttributeError since __privMeth is private
#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class Computer:
    def __init__(self, price):
        self.__max_price = price  # Private attribute

    def sell(self):  # Method to display the selling price
        print(f"The selling price is: {self.__max_price}")

    def set_max_price(self, price):  # Setter method to change the private attribute
        self.__max_price = price

# Creating an object of the class
computer = Computer(1000)
computer.sell()  # Display the initial price

# Changing the max price using the setter method
computer.set_max_price(1500)
computer.sell()  # Display the updated price
#Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.
class Point:
    def __init__(self, x, y):
        self.x = x  # Setting the x coordinate
        self.y = y  # Setting the y coordinate

    def get_coordinates(self):
        return f"Point({self.x}, {self.y})"  # Returning the coordinates in Point format

# Creating an object of the class
point = Point(3, 4)
print(point.get_coordinates())  # Printing the Point
#Write a Python class to reverse a string word by word.
class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage
reverser = StringReverser("Hello World")
print(reverser.reverse_words())  # Output: "World Hello"