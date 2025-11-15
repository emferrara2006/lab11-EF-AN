"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/emferrara2006/lab11-EF-AN.git
# Partner 1: Ethan Ferrara
# Partner 2: Andres Noguera (Didn't respond to me at all)

import math

# First example
def square_root(a):
	if  a < 0:
		raise ValueError("'a' cannot be negative") 
	else:
		return math.sqrt(a)

def hypotenuse(a ,b): return math.hypot(a ,b)

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a,b):
	if a == 0:
		raise ZeroDivisionError("Cannot divide by zero")
	else:
		return b / a

def logarithm(a, b):
	if a <= 0:
		raise ValueError("'a' cannot be less than or equal to 0")
	elif a == 1:
		raise ValueError("'a' cannot be equal to 1")
	elif b <= 0:
		raise ValueError("'b' cannot be less than or equal to 0")
	else:
		return math.log(b, a)

def exponent(a, b): return a**b
