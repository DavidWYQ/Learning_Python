# A hash is a one line comment

# print as a function.
print("Hello World")

# Getting user input
input("Name: ")

# Setting user input to a variable. Returns a str value
name = input("Name: ")
age = input("Age: ")


# Print output concatenated (space between data and "," appears to be optional)
print("Hello" , name , "you are" , age , "years old")

# Use int or float to covert from str to numerical input
print(int(age))
print(int(age) - 10)

# or at input
# age = input(int(age))
# age = age - 10
# print(age)



# Operands: + - * / normal. for x to power of y use ** - x ** Y . 
# / always returns a float.
#  // returns interger. 
# % returns the mod.


# Conditional Operators
# Return a True or False value
# > , < , <= , >= , == , !=
# Use == for equal to, using just = will likely try and set the left hand side of the argument as a variable.


# Methods
# Take the variable hello set to "hello"
# This will have the 'class' of string.
# using function type returns the class of the variable hello

hello = "hello"
print(type(hello))

# Classes have methods that can be applied to them.
# Methods are preceded by a "." eg .upper()

hello = "hello".upper()
print(hello)

#Alternate
print(hello.lower())

