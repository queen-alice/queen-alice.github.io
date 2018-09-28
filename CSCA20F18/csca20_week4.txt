CSCA20 Week 4 Notes
Objectives:
    1. Pratice with help() and dir()
    2. Practice writing boolean expression
    3. Write functions involving type str
    
1. Practice with help() and dir()
----------------------------------------------------------------------
What is help()?
- The help() method calls the build-in Pyton help system.
- It generates the help of the given object(int, str, float...)

How to call it?
- help(object)
example: call help(str) in the python shell
----------------------------------------------------------------------
What is dir()?
- An essential built-in function in python that provides information of the
given input

How to call it?
- dir()
Without an argument, it returns the list of names in the current local scope
- dir(object)
With an argument, it attempts to return a list of attributes to the
input object.
example(in shell)
-----------------------------------------------------------------------
-----------------------------------------------------------------------

2. Practice writing boolean expression
From last week,
There are 6 common comparision operators:
a < b
a > b
a == b
a != b (a is not equal to b)
a <= b (a less than or equal to b)
a >= b (a greater than or equal to b)

There are 3 logical operators:
and, or, not

example: 
a = 5
b = 10
(1) a!=b or a == b 
(2) a > b and a > 5
(3) a <= b or a != b
(4) a != b  and b <= 10
(5) a < 3  or b < 8
(6) a > 6 and a <= 5

-----------------------------------------------------------------------
-----------------------------------------------------------------------

3. Write functions involving type str
What is a string? 
- String literals in python are surrounded by either single quotation marks,
or double quotation marks.
- To get all the build-in methods of type str, try type help(str) in the shell
What is the length of a string?
- Number of characters in a string
What is the index of a string?
- the index of a string tells you the location of a specific character in
a string
What is a substring?
- A substring is a sequence of characters inside of a string
How to slice a string?
- string[a:b] gives a substring that starts at the index a and ends with the
index b but does not include b.
- string[-1] gives the last character in string.

------------------------------------------------------------------------
How to use string methods?
- find the length of a string 

- find the number of the occurrences of a substring in a string

- convert a string into all capital letters

- return a string with the trialing whitespace removed


