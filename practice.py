# 30 questions task(6 august 2026 )

#1
# def is_positive(num):
#     if num%2 == 0:
#         print("even")
#     else:
#         print("odd")
# is_positive(56)

#2
# def is_positive(num):
#     return num>0
# result = is_positive(56)

# First n odd numbers ka sum: 1 + 3 + 5 + ... + (2n - 1) = n^2
# def sum_first_n_odd_numbers(n):
# 	return n ** 2
# print(sum_first_n_odd_numbers(5))
# print(result)

# #3
# def find_max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# result = find_max(10,25)
# print(result)

##4
# def find_min(a,b):
#     if a<b:
#      return a
#     else:
#        return b
# result=find_min(13,90)
# print(result)


##5
# def check_vowel(letter):
#     return letter.lower() in "aeiou"
# print(check_vowel("e"))

##6
# def check(x):
#     if x>5 or x<1:
#         return True
#     else:
#         return False
    
# result = check(2)
# print(result)

###7
# def area_of_rectangle(l,w):
#     return(l*w)
# result=area_of_rectangle(20,30)
# print(result)

###8
# def Full_name(first,last):
#     return first+" " +last
# result = Full_name("ranjeet","yadav")
# print(result)

# ###9
# def greet(name="Guest"):
#     print(f"hello {name}")
# greet()
# greet("ranjeet")


###10
# def add(a,b):
#     return(a+b)
# result=add(2,3)
# print(result)

###11
# square=lambda n: n*n
# print(square(9))

##12
# def power(base,exponent=2):
#     return base**exponent
# print(power(5))
# print(power(2,3))

##13
# cube =lambda x: x*x*x
# print(cube(3))

##14
# is_even=lambda X: X%2 == 0
# print(is_even(23))

##15
# check_greater=lambda a,b: a>b
# print(check_greater(23,14))

# ##16
# def multiply(a,b,c =0):
#     result= a*b*c
#     return result
# print(multiply(10,20,30))

##17
# def sum_0f_three(a,b,c=0):
#     return a+b+c
# print(sum_0f_three(10,20,30))

##18
# def repeat_word(word,time=3):
#     return word* time
# print(repeat_word("Hi"))

##19
# def count(a):
#     if a>10:
#       return
#     print(a)
#     count(a+1)
# count(1)

##20
# def factorial(n):
#     if n == 1:
#         return 1
#     return n* factorial(n-1)
# print(factorial(5))

##21
# def area(length=5,width=4):
#     return length*width
# print(area())
# print(area(10))

##22
# def check_grade(score,passing_marks=40):
#     if score>=passing_marks:
#         return"pass"
#     return "Fail"
# print(check_grade(35))
# print(check_grade(35,30))

##23
# def add_number():
#     num1=int(input("enter first number"))
#     num2=int(input("enter second number"))
#     print("sum:", num1+num2)
# add_number()

##24
# def check(x)
#     if x>5 or x<100:
#         return "A"
#     elif x

##25
# def value(x,y):
#     if x==y:
#        return "A"
#     elif y % x == 0:
#         return "B"
#     else:
#       return "C"
# result =value(34,55)
# print(result)

##26
# def value(x,y):
#     if x % 5 == 0:
#       if x % y==0:
#          print(True)
#       else:
#          print(False)
#     else:
#      print(False)
# value(12,23)

##27
# def check(text):
#     if "a" in text:
#         print("exist")
#     else:
#         print("not exist")
# check("python")

###28
# def check(a):
#     if a!=0:
#         if a % 2 != 0:
#             print("odd")
#         else:
#             print("even")
#     else:
#         print("zero")
# check(9)

##29
# def  check(x):
#     if x>5:
#         return "saved"
#     elif x>2:
#         return "A"
#     else:
#         return "B"
# result=check(4)

##30
# def check(x):
#     if x != 0 and x%2 == 0 and x%3 == 0:
#         print("divisible by 2 and 3")
#     else:
#         print("condition failed")
# check(18)



''' revise on 22 september 2026'''

##Example 1
# def check(num):
#     if num>0:
#         print("Positive")
#         if num%2==0:
#            print("Even")
#         else:
#            print("Odd")
#     elif num<0:
#         print("negetive")
#     else:
#         return("Zero")
# check(-30)

##Example 2
# def check(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# check(80)

##Example 3
# def check(a,b,c):
#     if a<b>c:
#         return "b is great"
#     elif b<a>c:
#         return "a is great"
#     else:
#         return "c is great"
# result=check(8,9,10)
# print(result)

##Example 4
# def check(marks):
#     if marks>=90:
#         return "Grade A"
#     elif marks>=75:
#         return "Grade B"
#     elif marks>=60:
#         return "Grade c"
#     elif marks>=40:
#         return "Grade D"
#     else:
#         return "Fail"
# result=check(90)
# print(result)

##Example 5
# def check(year):
#     if year%4==0:
#         if year%400==0:
#            if year%100==0:
                
#             print("leap year")
#     else:
#         print("Not leap year")
# check(2025)

##Example 6
# def check_age(age):
#     if age>18:
#         print("Adult")
#     else:
#         print("Minor")
# check_age(56)

##Example 7
# day=3
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid day")

##Example 8
# def add(a,b):
#     print(a+b)
# add(5,4)

##Example 9
# def greet(name,age,city,course):
#     print(f" my name is {name} my age is {age} and I live in {city} my course is {course}")
# greet("ranjeet",20,"jaipur","python")

##Example 10
# def area(a,b):
#     print("area:",a*b)
# area(20,20)

##Example 11
# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

##Example 12
# add= lambda a,b: a+b
# print(add(3,4))

##Example 13
# def count(a):
#     if a<0:return
#     print(a)
#     count(a-1)
# count(8)

##METHOD 2
# def count(n):
#     print(n)
#     if n==0:
#         return
#     else:
#         count(n-1)
# count(100)

##METHOD 3
# def count(n):
#     print(n)
#     if n>0:
#         count(n-1)
# count(15)

##METHOD 4
# def count(n):
#     while n>=0:
#         print(n)
#         n-=1
# count(8)

##Example 13
# name="ranjeet"
# name="ashok"
# if name==name and name=="ranjeet":
#     name+="alok"
#     print(name)

##Example 14
# def count(n):
#     print(n)
#     if n==0:
#         return
#     count(n-1)
# count(5)


#### TASk 7 QUESTION TASK 7 AUGUST 2026  ####
##1
# def check_largest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# result= check_largest(12,13,14)
# print(result)

##2
# def grade(percentage):
#     if percentage>90:
#         return "grade A"
#     elif percentage>80:
#         return "grade B"
#     elif percentage>70:
#         return "grade c"
#     elif percentage>60:
#         return "grade D"
#     else:
#         return "F"
# result = grade(89)
# print(result)

###3
# def area_of_circle(radius):
#     return 3.14*radius**2
# area = area_of_circle(5)
# print(f"Area={area}")
# if area > 100:
#     print(True)
# else:
#     print(False) 

###4
# def leap(year):
#    if year%4==0:
#        print("leap year")
#    else:
#        print("not leap year")
# leap(2024)

# ###5
# def check_middle_number(a,b,c):
#     if b>a<c:
#         return a
#     elif a>b<c:
#         return b
#     else:
#         return c
# result = check_middle_number(12,13,14)
# print(result)

###6
# def check_number(num):
#     if num%2==0 and num%3==0:
#         return "divisible by 2 and 3"
#     else:
#         return "not divisible by 2 and 3"
# result = check_number(12)
# print(result)

###7
# a=5
# b=3
# a,b=b,a
# print("a=",b)
# print("b=",a)


#TASK 20 QUESTION TASK 10 AUGUST 2###
#Question 1
# def add(a,b):
#     return a+b
# result = add(9,5)
# print(result)

#Question 2
# def greet(name="Guest"):
#     print("Hello",name)
# greet()
# greet("ranjeet")

#Question 3
# def power(number,exponent=2):
#     return number**exponent
# print(power(5)) #25
# print(power(5,3)) #125

#Question 4
# square=lambda n: n*n
# print(square(3)) #9

#Question 5
# multiply= lambda a,b:a*b
# print(multiply(4,5)) #20

#Question 6
# km_to_miles = lambda km: km * 0.621
# print(km_to_miles(10))   # Output: 6.21

#Question 7
# def count(n):
#     if n==0: return
#     print(n+1)
#     count(n)
# count(1)

#Question 8
# def is_even(a):
#     if a%2 == 0:
#         return True
#     else:
#         return False
# result=is_even(3)
# print(result)

#Question 9
# def factorial(n):
#     if n == 1:
#         return 1
#     return n* factorial(n-1)
# print(factorial(5))

#Question 10
# length= lambda text: len(text)
# print(length("hello"))

#Question 11
# def check(x):
#     if x>0:
#         return "Positive"
#     if x<0:
#         return "Negative"

# print(check(4))

#Question 12
# def minute_to_second(minutes):
#  return minutes*60
# print(minute_to_second(5))

#Question 13
# def make_upparcase(text):
#     return text.upper()
# print(make_upparcase("python"))

#Question 14
# def join_words(first_word,second_word):
#     return first_word + " " + second_word
# print(join_words("Hello","world"))

#Question 15
# def hours_to_minutes(hours):
#     return hours*60
# print(hours_to_minutes(2))

#Question 16
# def count(n):
#     if n<0: return
#     count(n-1)
#     print(n)
# count(5)

#Question 17
# def get_sum(n):
#     if n<0: return 0
#     return n+get_sum(n-1)
# print(get_sum(9))

#Question 18
# def say_hello(n):
#     if n==0: return
#     print("Hello")
#     say_hello(n-1)
# say_hello(3)

#Question 19
# def show_stars(n):
#     if n==0: return
#     print("*")
#     show_stars(n-1)
# show_stars(4)

#Question 20
# def student_info(name, course="python"):
#     print(name)
#     print(course)
# student_info("Rahul")
# student_info("rahul","java")

# def factorial(n):
#     if n==1:
#         return 1
#     return n* factorial(n-1)
# print(factorial(5))

## daily task 17 AUGUST 2026
# add=lambda a,b=10:a+b
# print(add(5,))

#Q2
# def calculate_interest(base_amount, rate=5):
#     return base_amount * rate / 100


# # Default rate use hoga: 5%
# print(calculate_interest(1000))        # 50.0

# # Rate override hoga: 12%
# print(calculate_interest(1000, 12))    # 120.0

#Q3
# discount = lambda amount, rate=10: amount * rate / 100

# # Default discount rate: 10%
# print(discount(1000))       # 100.0

# # Different discount rates
# print(discount(1000, 20))   # 200.0
# print(discount(500, 5))     # 25.0
# print(discount(2500, 15))   # 375.0

#Q4
# percentage = lambda obtained, total=100: (obtained / total * 100) if total != 0 else 0

# # Default total = 100
# print(percentage(75))          # 75.0

# # Custom total
# print(percentage(45, 60))      # 75.0

# # total = 0: error nahi aayega
# print(percentage(50, 0))       # 0

# def factorial(n):
#     if n==1:
#         return n
#     return n* factorial(n-1)
# print(factorial(5))

# def power(a, b):
#     # Negative exponent
#     if b < 0:
#         return 1 / power(a, -b)

# # Base case
# if b == 0:
#         return 1

#     # Recursive case
#     return a * power(a, b - 1)


# print(power(2, 3))    # 8
# print(power(5, 0))    # 1
# print(power(2, -3))   # 0.125



"""
=== 100+ LOGICAL PROGRAMMING QUESTIONS ===
Topics: Variables, Data Types, Operators, Conditions, Functions, Lambda, Recursion
"""

# ============ SECTION 1: VARIABLES & DATA TYPES (10 Q) ============

# Q1: Variable assignment और print करें
# Declare करें: name="Ranjeet", age=25, height=5.9
# सभी को print करें

# def intro(name,age,height):
#     return name,age,height
# result=intro("ranjeet",25,'5\'7" ')
# print(result)

# Q2: Type checking
# किसी भी variable का type check करो using type()
# variable=89
# print(type(variable))
# Q3: Multiple assignment
# a, b, c = 10, 20, 30 - सभी को print करो
# a,b,c,=10,20,30
# print(a)
# print(b)
# print(c)

# Q4: Type conversion
# String "123" को integer में convert करो फिर add करो 10 से

# num="123"
# num=int("123")
# result=int(num+10)
# print(result)
# Q5: List, Tuple, Dictionary
# एक list, tuple, dictionary create करो और access करो

# Q6: String operations
# text = "Python" - length, uppercase, lowercase निकालो

# Q7: List operations
# list = [1,2,3,4,5] - append, remove, slicing करो

# Q8: Dictionary operations
# dict = {"name": "Ranjeet", "age": 25} - keys, values निकालो

# Q9: Set operations
# set1 = {1,2,3}, set2 = {3,4,5} - union, intersection निकालो

# Q10: Boolean values
# True/False से कोई condition check करो


# ============ SECTION 2: OPERATORS (15 Q) ============

# Q11: Arithmetic Operators
# a=20, b=3 - सभी arithmetic operators (+, -, *, /, //, %) का result निकालो
# def calculate(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a//b)
#     print(a**b)
#     print(a%b)
#     print((a+b)/2)
# calculate(5,4)


# Q12: Comparison Operators
# 15 > 10, 20 == 20, 5 != 5 - results देखो
# print(15>10)
# print(20==20)
# print(5!=5)

# Q13: Logical AND
# 5 > 3 and 10 < 20 - क्या True है?
# print(5>3 and 10< 20)


# Q14: Logical OR
# 5 > 10 or 10 > 5 - क्या True है?
# print(5>10 or 10>5)


# Q15: Logical NOT
# not (5 > 3) - क्या result है?
# print(not(5>3))


# Q16: Membership Operator (in)
# "a" in "apple" - True/False?
# print("a" in "apple")


# Q17: Membership Operator (not in)
# 5 not in [1,2,3,4] - True/False?
# print(5 in [1,2,4,3,5])

# Q18: Identity Operator (is)
# a = [1,2,3]; b = a; a is b - True/False?
# a=[1,2,3]
# b=[1,2,3]
# b=a
# print(a is b)

# Q19: Identity Operator (is not)
# a = [1,2,3]; b = [1,2,3]; a is not b - True/False?
# a=[1,2,3]
# b=[1,2,3]
# print(a!=b)

# Q20: Chained comparison
# 10 < 20 < 30 - क्या True है?

# print(10<20<30)

# Q21: Assignment operators
# a = 5; a += 3 - क्या होगा?
# a=5
# a+=3
# print(a)

# Q22: Bitwise AND
# 5 & 3 - क्या result है?
# print(5 & 3)

# Q23: Bitwise OR
# 5 | 3 - क्या result है?
# print(5|3)

# Q24: Modulus with negative numbers
# -10 % 3 - क्या result है?

# Q25: Power operator
# 2 ** 8 - क्या result है?
# print(2**8)


# ============ SECTION 3: CONDITIONAL STATEMENTS (20 Q) ============

# Q26: Simple if
# score = 85
# if score > 80:
#     print("Good")
# else:
#     print("bad")

# Q27: if-else
# age = 15
# if age >= 18: print("Adult")
# else: print("Minor")

# Q28: if-elif-else
# marks = 75
# if marks > 90: print("A")
# elif marks > 80: print("B")
# elif marks > 70: print("C")
# else: print("F")

# Q29: Nested if
# x = 10
# if x > 5:
#     if x > 15: print("Greater than 15")
#     else: print("Between 5 and 15")

# Q30: Ternary operator
# age = 20
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# Q31: Multiple conditions with AND
# score = 85, attendance = 95
# if score > 80 and attendance > 90:
#     print("Pass")

# Q32: Multiple conditions with OR
# age = 12, guardian_permission = True
# if age >= 18 or guardian_permission:
#     print("Can join")

# Q33: NOT operator in condition
# is_valid = False
# if not is_valid:
#     print("Invalid")

# Q34: Checking if number is positive, negative, or zero
# num = -5
# if num > 0: print("Positive")
# elif num < 0: print("Negative")
# else: print("Zero")

# Q35: Checking leap year
# year = 2024
# if year % 4 == 0 and year % 100 != 0:
#     print("Leap year")
# elif year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not leap year")

# Q36: Even or Odd
# num = 17
# if num % 2 == 0: print("Even")
# else: print("Odd")

# Q37: Divisible check
# num = 15
# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible by both 3 and 5")

# Q38: Grade assignment
# percentage = 78
# if percentage >= 90: grade = "A"
# elif percentage >= 80: grade = "B"
# elif percentage >= 70: grade = "C"
# else: grade = "F"
# print(grade)

# Q39: Name starts with 'r' (आपका original question)
# name = input("Enter name: ")
# if name.lower().startswith("r"):
#     print("Condition failed - Name starts with r")
# else:
#     print("Condition passed")

# Q40: Vowel checker
# letter = "a"
# if letter.lower() in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")

# Q41: Triangle validity
# a, b, c = 3, 4, 5
# if a + b > c and b + c > a and a + c > b:
#     print("Valid triangle")

# Q42: Temperature range
# temp = 25
# if temp < 0: print("Freezing")
# elif temp < 15: print("Cold")
# elif temp < 25: print("Cool")
# else: print("Hot")

# Q43: Password strength
# password = "Pass123!"
# if len(password) >= 8 and any(c.isupper() for c in password):
#     print("Strong")

# Q44: Login check
# username = "admin", password = "1234"
# if username == "admin" and password == "1234":
#     print("Login successful")

# Q45: Age group checker
# age = 35
# if age < 13: group = "Child"
# elif age < 20: group = "Teen"
# elif age < 60: group = "Adult"
# else: group = "Senior"


# ============ SECTION 4: FUNCTIONS & RETURN (20 Q) ============

# Q46: Basic function
# def greet():
#     print("Hello World")
# greet()

# Q47: Function with parameters
# def add(a=1, b=2):
#     return a + b
# print(add(5, 3))
# print(add())

# Q48: Function with multiple parameters
# def calculate(x, y, z):
#     return x + y + z
# print(calculate(10, 20, 30))

# Q49: Function returning boolean
# def is_positive(num):
#     return num > 0
# print(is_positive(-5))

# Q50: Function with default parameter
# def greet(name="Guest"):
#     return f"Hello {name}"
# print(greet())
# print(greet("Ranjeet"))

# Q51: Function with multiple default parameters
# def info(name="Unknown", age=0):
#     return f"{name} is {age} years old"
# print(info())
# print(info("Rahul", 25))

# Q52: Function returning tuple
# def get_coordinates():
#     return 10, 20
# x, y = get_coordinates()
# print(x, y)

# Q53: Function returning list
# def get_numbers():
#     return [1, 2, 3, 4, 5]
# print(get_numbers())

# Q54: Function with conditional return
# def check_grade(marks):
#     if marks >= 90: return "A"
#     elif marks >= 80: return "B"
#     else: return "C"
# print(check_grade(85))

# Q55: Function without explicit return
# def print_square(n):
#     print(n ** 2)
# print_square(5)  # prints 25, returns None

# Q56: Function calling another function
# def square(n):
#     return n * n
# def cube_plus_square(n):
#     return n ** 3 + square(n)
# print(cube_plus_square(3))

# Q57: Function with variable arguments (*args)
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2, 3, 4, 5))

# Q58: Function with keyword arguments (**kwargs)
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_info(name="Ranjeet", age=25, city="Delhi")

# Q59: Scope - Local variable
# def test():
#     x = 10
#     print(x)
# test()
# # print(x)  # Error - x not defined globally

# Q60: Scope - Global variable
# x = 5
# def test():
#     global x
#     x = 10
# test()
# print(x)  # 10

# Q61: Return multiple values
# def get_name_age():
#     return "Ranjeet", 25
# name, age = get_name_age()
# print(name, age)











# Q62: Function with docstring
# def add(a, b):
#     """यह function दो numbers को add करता है"""
#     return a + b
# print(add.__doc__)

# Q63: Function returning function
# def outer():
#     def inner():
#         return "Hello"
#     return inner
# func = outer()
# print(func())

# Q64: Recursive function - Factorial
# def factorial(n):
#     if n == 1: return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# Q65: Recursive function - Fibonacci
# def fibonacci(n):
#     if n <= 1: return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(6))


# ============ SECTION 5: LAMBDA FUNCTIONS (15 Q) ============

# Q66: Simple lambda
# square = lambda x: x ** 2
# print(square(5))

# Q67: Lambda with multiple parameters
# add = lambda a, b: a + b
# print(add(3, 7))

# Q68: Lambda with default parameter
# greet = lambda name="Guest": f"Hello {name}"
# print(greet())

# Q69: Lambda in map()
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)

# Q70: Lambda in filter()
# numbers = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)

# Q71: Lambda with if-else
# check_age = lambda age: "Adult" if age >= 18 else "Minor"
# print(check_age(20))

# Q72: Lambda with multiple conditions
# validate = lambda x, y: "Valid" if x > 0 and y > 0 else "Invalid"
# print(validate(5, 3))

# Q73: Lambda for conversion
# km_to_miles = lambda km: km * 0.621
# print(km_to_miles(10))

# Q74: Lambda in sorted()
# students = [("Ranjeet", 85), ("Rahul", 90), ("Priya", 78)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# Q75: Lambda returning boolean
# is_even = lambda n: n % 2 == 0
# print(is_even(4))

# Q76: Lambda for string operations
# reverse_string = lambda s: s[::-1]
# print(reverse_string("hello"))

# Q77: Lambda for list operations
# sum_list = lambda lst: sum(lst)
# print(sum_list([1, 2, 3, 4, 5]))

# Q78: Lambda with nested conditions
# grade = lambda marks: "A" if marks > 90 else "B" if marks > 80 else "C"
# print(grade(85))

# Q79: Lambda for maximum value
# max_value = lambda a, b, c: max(a, b, c)
# print(max_value(10, 20, 15))

# Q80: Lambda in list comprehension
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * x if x % 2 == 0 else x, numbers))
# print(result)


# ============ SECTION 6: INPUT/OUTPUT (10 Q) ============

# Q81: Simple input
# name = input("Enter your name: ")
# print(f"Hello {name}")

# Q82: Input and convert
# age = int(input("Enter age: "))
# print(f"You are {age} years old")

# Q83: Multiple inputs
# a = int(input("First number: "))
# b = int(input("Second number: "))
# print(f"Sum: {a + b}")

# Q84: Input with default handling
# name = input("Enter name (default: Guest): ") or "Guest"
# print(name)

# Q85: String input operations
# text = input("Enter text: ")
# print(f"Length: {len(text)}, Uppercase: {text.upper()}")

# Q86: Input validation
# while True:
#     age = int(input("Enter age (18-60): "))
#     if 18 <= age <= 60: break
#     print("Invalid!")

# Q87: Float input
# price = float(input("Enter price: "))
# discount = price * 0.1
# print(f"Final price: {price - discount}")

# Q88: List input
# numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
# print(f"Sum: {sum(numbers)}")

# Q89: Formatted output
# name, age = "Ranjeet", 25
# print(f"Name: {name:>10}, Age: {age:>3}")

# Q90: Print with separator
# print("Apple", "Banana", "Cherry", sep=", ")


# ============ SECTION 7: MIXED QUESTIONS (10 Q) ============

# Q91: Function + Conditional + Input
# def calculate_grade():
#     marks = int(input("Enter marks: "))
#     if marks >= 90: return "A"
#     elif marks >= 80: return "B"
#     else: return "C"
# print(calculate_grade())

# Q92: Lambda + List + Conditional
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(filter(lambda x: x % 2 == 0 and x > 5, numbers))
# print(result)

# Q93: Recursion + Conditional
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     if len(s) <= 1: return True
#     if s[0] != s[-1]: return False
#     return is_palindrome(s[1:-1])
# print(is_palindrome("racecar"))

# Q94: Function + Multiple Parameters + Default
# def calculate(x, y, operation="+"):
#     if operation == "+": return x + y
#     elif operation == "-": return x - y
#     elif operation == "*": return x * y
#     elif operation == "/": return x / y if y != 0 else "Division by zero"
# print(calculate(10, 5))
# print(calculate(10, 5, "-"))

# Q95: Lambda + Map + Filter
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, data)))
# print(result)

# Q96: Nested functions
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
# add_5 = outer(5)
# print(add_5(3))

# Q97: String manipulation + Function
# def word_count(text):
#     words = text.split()
#     return {word: words.count(word) for word in set(words)}
# print(word_count("python python java python"))

# Q98: List + Lambda + Conditional
# scores = [45, 78, 92, 34, 88, 65]
# passed = list(filter(lambda x: x >= 60, scores))
# print(f"Passed: {passed}, Count: {len(passed)}")

# Q99: Tuple unpacking + Function
# def get_user_info():
#     return ("Ranjeet", 25, "Delhi")
# name, age, city = get_user_info()
# print(f"{name}, {age}, {city}")

# Q100: Dictionary + Lambda + Conditional
# students = {"Ranjeet": 85, "Rahul": 92, "Priya": 78}
# top_scorer = max(students.items(), key=lambda x: x[1])
# print(f"Top scorer: {top_scorer[0]} with {top_scorer[1]} marks")

# Q101: Type checking + Conditional
# def process_input(value):
#     if isinstance(value, int): return value ** 2
#     elif isinstance(value, str): return value.upper()
#     elif isinstance(value, list): return len(value)
#     else: return "Unknown type"
# print(process_input(5))
# print(process_input("hello"))
# print(process_input([1, 2, 3]))

# Q102: Error handling (bonus)
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))

# Q103: Lambda + List comprehension
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat = [item for row in matrix for item in row]
# squared = list(map(lambda x: x ** 2, flat))
# print(squared)

# Q104: Function + Recursion + String
# def count_character(text, char, index=0):
#     if index >= len(text): return 0
#     return (1 if text[index] == char else 0) + count_character(text, char, index + 1)
# print(count_character("hello", "l"))

# Q105: Complex conditional + Lambda
# def get_discount(age, membership):
#     discount_func = lambda a, m: 20 if m and a > 50 else 10 if m else 5 if a > 50 else 0
#     return discount_func(age, membership)
# print(get_discount(55, True))
# print(get_discount(30, False))

# print("=" * 60)
# print("100+ LOGICAL PROGRAMMING QUESTIONS")
# print("=" * 60)
# print("\nउपरोक्त सभी questions को uncomment करके एक-एक करके solve करें")
# print("हर question के लिए अपना output check करें!")
# print("=" * 60)










# 1. Write a function that prints whether a number is even or odd.
# def check(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "odd"
# print(check(8))

# 2. Write a function that returns True if a number is positive.
# def check(num):
#     if num>0:
#         return True
#     else:
#         return False
# print(check(40+(-50)))

# 3. Write a function to find the larger of two numbers.
# def check(a,b):
#     if a>b:
#         return "a is larger"
#     elif a<b:
#         return "b is larger"
#     else:
#         return "both are equal"
# print(check(89,56))
#second tarika
# def check(a,b):
#     if a>b:
#         return a
#     return b
# def show_result(a,b):
#     result=check(a,b)
#     print("Larger number is:",result)

# show_result(89,56)


# 4. Write a function to find the smaller of two numbers.
# def check(a,b):
#     if a<b:
#         return "a is smaller"
#     else:
#         return "b is smaller"
    

# 5. Write a function that checks if a letter is a vowel.
# def check(letter):
#     return letter.lower() in "aeiou"

# print(check("e"))
# print(check("b"))

# 6. Write a function that returns the area of a rectangle.
# def area_of_rectangle(l,w):
#     return l*w
# print(area_of_rectangle(8,9))

# 7. Write a function that returns the full name of a person.
# first_name="Ranjeet"
# last_name="Rao"
# full_name=first_name+" "+last_name
# print(full_name)

# 8. Write a function with a default parameter for greeting.
# def greet(name,age):
#     name= input("enter your name")
#     age=int(input("enter your age"))
#     print(f"hello {name}, your age is {age}")
# greet()

# def greet(name="guest",age="above 18"):
#     print(f"hello {name} your age is {age}")
#     return name,age
# greet()
# greet("ranjeet",20)

# 9. Write a lambda function to square a number.
# square=lambda n: n*n
# print(square(9))

# 10. Write a function to add two numbers and print the result.
# def add(a,b):
#     return a+b
# print("Addition is:",add(8,9))

# Logical Questions for Practice

# Yeh questions aise hain jo human brain ke liye logical thinking ko improve karte hain.

# ## Easy
# 1. Write a Python program to print the sum of first 10 natural numbers.
# def natural_number_sum(n):
#     if n>10:
#         return 10
#     return (n*(n+1)/2)
# print(natural_number_sum(10))
# 2. Write a Python program to find whether a number is even or odd.
# def check(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(check(1110))
# 3. Write a Python program to check whether a person is eligible to vote.
# def age():
#     if age>=18:
#         return "eligible for vote"
#     elif age>=90:
#         return "not eligible for vote because more age"
#     else:
#         return "not eligible for vote"
# print(age(13))

# 4. Write a Python program to find the largest of two numbers.
# def to_find_largest(a,b):
#     if a>b:
#         return "a is greater than b"
#     elif a<b:
#         return "b is greater than a"
#     else:
#         return "Both are equal"
# print(to_find_largest(9,8))
# 8. Write a Python program to reverse a number.################################

# 9. Write a Python program to count how many vowels are in a string
# def count(s):
#     if s=="":
#         return 0
#     else:
#         if s[0] in "aeiou":
#             return 1 + count(s[1:])
#         else:
#             return 0 + count(s[1:])
# print(count("ranjeet"))

# 10. Write a Python program to swap two numbers without using a third variable.
# a=4
# b=5
# a,b=b,a
# print("a=",a)
# print("b=",b)

# ## Medium
# 11. Write a Python program to check whether a string is a palindrome.
# def is_palindrome(s):
#     if s=="" or len(s)==1:
#         return True
#     else:
#         if s[0]==s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False
# print(is_palindrome("level"))

# 12. Write a Python program to find the sum of digits of a number using recursion.
# def sum(d):
#     if d==0:
#         return 0
#     else:
#         return d%10 +sum(d//10)
# print(sum(1234567))

# 13. Write a Python program to print the multiplication table of a given number.
# def table(n,i=1):
#     if i>10:return
#     print(n*i)
#     table(n,i+1)
# table(90)
# table(8)

# 14. Write a Python program to find the largest digit in a number.
# num=29345019
# def largest(i,lar):
#     print(i)
#     if i=="":
#         print(lar)
#         return
#     if int(i[0])>=lar:
#         lar=int(i[0])
#         largest(i[1::],lar)
#     else:
#         largest(i[1::],lar)
# largest(str(num),int(str(num)[0]))

# # 15. Write a Python program to count the number of characters in a string without using len().
# def count(str,char):
#     if str=="":
#         print(char)
#         return
#     char+=1
#     count(str[1::],char)
# count("hello",0)

# 16. Write a Python program to print the following pattern:
#    *
#    **
#    ***
#    ****

# def star1(i):
#     if i>4: return
#     print(i*"*")
#     star1(i+1)
# star1(1)
# 17. Write a Python program to print the following pattern:
#    ****
#    ****
#    ****
# def star2(i):
#     if i>4:return
#     print(4*"*")
#     star2(i+1)
# star2(1)
# 18. Write a Python program to find the Fibonacci series up to n terms.
# def Fibonacci(i)
# 19. Write a Python program to check whether a year is a leap year.
# def check():
#     Year=int(input("enter year"))
#     if Year %4==0:
#         print("it a leap year")
#     else:
#         print("it is not a leep year")
# check()
'''
# 20. Write a Python program to calculate the sum of first n odd numbers.
# def odd_sum(o):
#  for i in range(1,o+1):
#     if i%2==1:
#        o+=i
#  return o
# print(odd_sum(10))
 


# def natural_sum(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# print(natural_sum(100))
'''
# ## Hard
# 21. Write a Python program to print a triangle pattern using recursion.
# for i in range(1,6):
#     for j in range(1,10):
#         if j==5-i+1 or j==5+i-1 or i==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 22. Write a Python program to find the GCD of two numbers using recursion.
# 23. Write a Python program to find the power of a number using recursion.
# 24. Write a Python program to check whether a number is prime using recursion.

# 25. Write a Python program to print the table of 7 using recursion.
# def table(i):
#     if i>10:return
#     print(i*7)
#     table(i+1)
# table(1)

# 26. Write a Python program to find the sum of first n natural numbers using recursion.
# n=int(input("Enter a number"))
# sum=0
# for i in range(n):
#     sum+=i
# print(sum)

# 27. Write a Python program to print numbers from n to 1 using recursion.
# n=(input("enter a number"))
# for i in range(n,1,-1):
#     print(i)

# 28. Write a Python program to count the number of digits in a given integer using recursion.


# 29. Write a Python program to calculate the sum of all elements in a list using recursion.
# marks=[1,2,3,4,5,6,7,8,9,10]
# total=0
# for i in marks:
#     total+=i
# print(total)

# 30. Write a Python program to find the maximum element in a list using recursion.
# marks=[1,2,3,4,5,6,7,8,9,0]
# maximum=0
# for i in marks:
#     maximum+=1
# print(maximum)#10

# ## Brainy / Logical
# 31. Write a Python program to guess a hidden number and keep asking until the correct number is found.
# secret_number = 3
# guess = 0
# while guess != secret_number:
#     guess = int(input('Guess the number (1-5): '))
#     if guess != secret_number:
#         print('Wrong! Try again.')
# print('You got it!')

# 32. Write a Python program to find the second largest number in an array.
# mark=[1,2,3,4,5,6,7]
# max=0
# sec_max=0
# for i in mark:
#     if max<i:
#         sec_max=max
#         max=i
#     elif sec_max<i:
#         sec_max=i
# print(sec_max)


# 34. Write a Python program to merge two lists and sort them.
# a=[1,2,3,4]
# b=[5,6,7,8]
# a.extend(b)
# print(a)#[1, 2, 3, 4, 5, 6, 7, 8]
# 35. Write a Python program to find the average of numbers entered by the user.

# 36. Write a Python program to count how many times a specific word appears in a sentence.
# 37. Write a Python program to check whether two strings are anagrams.
# 38. Write a Python program to print all even numbers between 1 and 100.
# 39. Write a Python program to print all odd numbers between 1 and 100.
# 40. Write a Python program to find the total number of uppercase letters in a string.

# ## Advanced
# 41. Write a Python program to solve the Tower of Hanoi problem using recursion.
# 42. Write a Python program to generate all permutations of a string using recursion.
# 43. Write a Python program to find all subsets of a list using recursion.
# 44. Write a Python program to check whether a given number is a perfect number.
# 45. Write a Python program to perform binary search recursively.
# 46. Write a Python program to find the total number of ways to climb stairs.
# 47. Write a Python program to reverse a list using recursion.
# 48. Write a Python program to flatten a nested list using recursion.
# 49. Write a Python program to count the number of occurrences of a digit in a number.   