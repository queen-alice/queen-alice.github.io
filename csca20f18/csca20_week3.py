CSCA20 Week 3 Notes

Objectives: 
1. Pratice working with variables
2. Pratice defining functions in editors
3. Pratice writing boolean expressions and conditional statements
4. Use the stylechecker
5. Demonstrate how to submit the exercises and labs

1. Variables and Types (From last week's tutorial)
What are variables? 
Variables act like a "storage location" for data in the program and a way
of naming information for later usage 
<variable name> = <the value you want to store>
-------------------------------------------------------------------------
What are data types?
It is the type of a variable.
You can use the built-in method type() to check what type of variable you
are working with 
Example:
    type("5.67")
    type(5.67)
    type(5.0)
    type(5)
--------------------------------------------------------------------------
Type Conversions by using methods int(), str(), float()
1. converting integers to floats
float(3)
2. converting floats to intergers
int(3.435)
3. converting with strings
we can convert numbers to strings 
str(3) 
str(3.456)
we can also convert strings to numbers
int('3')
float('3.456')
4. converting a value to boolean
bool(0)
-------------------------------------------------------------------------
-------------------------------------------------------------------------
2. Functions
What is a function? Why do we use functions? How to write a function?
def function_name(parameters):
    """ description of the function 
    
    Args:
        input variable
        
    #Returns:
        #output
    #"""
    code

Example (lecture):
def f(x):
    """The linear function f as defined in the slides
    
    Args:
        x: a number
        
    Returns:
        2 * x + 1
    """
    print('this code will be run')
    return 2 * x + 1
    print('this line will never run')

How to call the function f?


Example(volume of a cuboid):

volume = cuboid_volume(2, 4, 5)
print(volume)


------------------------------------------------------------------------
Note: What are the differences between the print() and return()

    return(): - you can only use "return" inside a function
              - values that are returned can be saved and re-used
              - return is used primarily to retrieve data that was
              modified/generated, at the end of a function call

    print(): - you can print anywhere in your program
             - printing a value doesn't save it. It only displays
             the value in the shell.
             - print statements are used to display information to
             the shell. This can be useful for debugging and testing.
             
--------------------------------------------------------------------------
--------------------------------------------------------------------------
3. Boolean expressions and contional statements
What is a boolean value?
They are of the data type bool! In python, here are two boolean values True and False.
What is a boolean expression?
A boolean expression is an expression that evaluates to a boolean value. 
(must be capitalized; python is case sensitive)


Example: 
a = 1
b = 5
Since a is not equal to b, the expression "a == b" evaluates to True
Since a is equal to 1, the expression "a == 1" evaluates to False
print(a == b)
print(a == 1)

There are 6 common comparision operators:
a < b
a > b
a == b
a != b (a is not equal to b)
a <= b (a less than or equal to b)
a >= b (a greater than or equal to b)

There are 3 logical operators:
and, or, not

Example:
The expression "a <= 10" evaluates to True and "a > 5" evaluates to False.
The expression "a <= 10 and a > 5" return ?
The expression "a <= 10 or a > 5" return ?
a = 1
b = 5
print(a <= 10 and a > 5)
print(a <= 10 or a > 5) 
print(a != b and a < 10)
print(b < 4 or b != 0)
-----------------------------------------------------------------------------
What is a contional statement? Why do we use conditional statements?
Provide us with the ability to check conditions and change the behaviour of
the program accordingly.
example 1: only possible case (only perform task1 if condition1 is met)
if condition1:
    perform task1

                        
example 2: 2 possible cases (either condition1 is met or not met)
if condition1:
    perform task1
else:
    perform task2

                        
example 3: 3 or more possible cases
if condition1:
    perform task1
elif condition2:
    perform task2
elif condtion3:
    perform task3
else:
    perform task4


example 4: nested conditional statements


example (cuboid_category):

def cuboid_category(h, w, l):
    """ Return which category the cuboid belongs to. 
    volumn < 50, cate 1
    50 <= volumn <= 200, cate 2
    volumn > 200, cate 3
    Args: 
       h: height of the cuboid in cm
       w: weight of the cuboid in cm
       l: length of the cuboid in cm
    Returns:
       category of the cuboid: positive integer
     
    """


    
Note: What are the differences between if and elif
Note: How many else blocks am I allowed to have?


-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
4. How to use the stylechecker?
PEP8 website
                        

