'''
Text Type (String)
'''

# s = "This is a single line string"
# print(s)
# print(type(s))

# =========================

# s = """this is a multiline 
# string example"""
# print(s)

# =========================

# find a character by index
# s = 'string sample'
# print(s[5])

# slicing
# s = 'string sample'
# print(s[7:])

# s = 'string sample'
# print(s[1:6])

# =========================
# immutable

# s = 'string sample'
# s[2] = 'o'
# print(s)

'''
Numeric Type (Integer, Float, Complex)
'''
# Integer
# x = 1232454657676
# print(type(x))

# Float
# Accurate up to 15-16 decimal places
# x = 0.231232454657676
# print(type(x))

# complex numbers
# x = 1+2j
# print(type(x))

'''
Sequence Type (List, Tuple, Range)
'''
# homogenous 
# x = []
# # List
# x = [10, 2.5, 'hello'] 
# print(x[2])
# print(x[1:3])

# # mutable (a list can be changed). 
# x[2] = 'python'
# print(x)

# # Tuple (immutable)
# Hetrogenous (mixed data types)
# tuple = ()

# =========================

# both of examples below are type tuples, adding a comma makes it a tuple, without a comma makes it a string.
# tuple = ("hello",)
# tuple = "hello",
# print(type(tuple))

# =========================

### A list is square brackets, a tuple is normal brackets (parentheses)

# tuple = ('cat', [4,3,2], (1,2,3))
# print(tuple[2])

# =========================

# immutable

# tuple = ('cat', [4,3,2], (1,2,3))
# tuple[2] = 10
# print(tuple)

# =========================

# Range

# x = range(10)
# for n in x: 
#   print(n)

'''
Mapping Type (Dictionary)
'''
# dict = {}
# print(type(dict))

# =========================
# dict is mutable

# dict = {'name': 'Kingsley', 'age': 37}
# print(dict['age'])
# print(dict.get('name'))

# dict['age'] = 26
# print(dict)

'''
Set Types
'''
# empty set having set = {} is an empty dictionary

# set = set()
# print(type(set))

# =========================

# mixed data types (all mutable)

# set = {3.2,"hi", (1,2,3)}
# print(type(set))
# # TypeError: 'set' object is not subscriptable
# print(set[0])

# ==========================
# no duplicates
# cannot call by index 

# set = {3.2,"hi", (1,2,3), "hi"}
# print(set)

# ==========================
# cannot have mutable (list) in a set
# set = {3.2,"hi", (1,2,3), [1,2,3]}
# # unhashable type: 'list'
# print(set)

'''
Boolean Type (True or False)
'''

# print(type(True))

# Boolean as numbers
# print(True == 1)
# print(False == 0)

# Interesting logic
# print(True + True)

# Not boolean operator
# print(not True)
# print (not False)

# And boolean operator
# print(True and False)
# print(True and True)
# print(False and False)

# Or boolean operator
# print(True or False)
# print(True or True)
# print(False or False)