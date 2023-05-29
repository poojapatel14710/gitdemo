# a = "khokho"
#
# b = len(a)
# if b%2 == 0:
#     c = a[0:b//2]
#     d = a[b//2:]
#     print(c)
#     print(d)
#
#     if c==d:
#         print("The entered string is symmetrical")
#
# p = "amaama"
# q = len(p)
# if q%2 ==0:
#     q1 = p[0:q//2]
#     q2 = p[q//2:]
#     j = -1
#     flag = 0
#     for i in range(0,q//2):
#         if p[i] == p[j]:
#             j -=1
#             pass
#         else:
#             print("Not planidrome")
#             flag = 1
#             break
#     if flag == 0:
#         print(" palindrome")



# To reverse words in a given string

# input string
# string = "geeks quiz practice code"
# # reversing words in a given string
# s = string.split()[::-1]
# print(" ".join(s))


test_str = "GeeksForGeeks"
# # remove 3rd position
l = []
#
# for i in range(0,len(test_str)):
#     if i != 2:
#         l.append(test_str[i])
# print("".join(l))


# # reverse string
# j = -1
# l = []
# for i in range(0,len(test_str)):
#     l.append(test_str[j])
#     j -= 1
# print("".join(l))

# Avoid Spaces in string length
# p = "geeksforgeeks 33 best"
# q =p.replace(" ", "")
# print(len(q))


# str = "0iouvjdf"
# vowels = ['a', 'e', 'i', 'o', 'u']
# not_vowels = []
# for i in vowels:
#     if i not in  str:
#         not_vowels.append(i)
#
# if not_vowels == []:
#     print("contain")
# else:
#     print(not_vowels)



# # Count the Number of matching characters in a pair of string
# a = "abcdefg"
# b = "efghijk"
# c = 0
# for i in range(0, len(a)):
#     for j in range(0, len(b)):
#         if a[i] ==b[j]:
#             c += 1
# print(c)


# # remove all duplicate
# a = "pooja"
# b = []
# for i in range(0,len(a)):
#     b.append(a[i])
#
# g = set(b)
# for i in g:
#     print(i)

import copy


l1 = [1,2,[3,4],5,6,7]
l2 = copy.copy(l1)
print(l2)
l2[1:3] = [8,9]

print(l2)
print(l1)

# l1 = [1,2,3,4,5,6,7]
# l2 = copy.deepcopy(l1)
# print(l2)
# l2[1:3] = [8,9]
# print(l2)
# print(l1)




# initializing list 1
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print(li1)
li1[2][0] = 7
print(li2)
print(li1)


# Python List Comprehension: Find all of the numbers from 1-1000 that are divisible by 7

list = []
for i in range(1,1001):
    if i % 7 == 0:
        list.append(i)

print(list)
l1 = [i for i in range(1,1001) if i % 7 == 0]
print(l1)


# Python List Comprehension: Find all of the numbers from 1-1000 that have a 3 in them
l1 = [i for i in range(1,1001) if "3" in str(i)]
print(l1)


# Python List Comprehension: Count the number of spaces in a string
string = 'the slow solid squid swam sumptuously through the slimy swamp'
l2 = [i for i in string if i == " "]
print(len(l2))


# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
str = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
vovewls = ['a', 'e', 'i', 'o', 'u', ' ']
l3 = [i for i in str if i not in vovewls]
print(l3)

# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
# Result would look like (index, value), (index, value)

l4 = ["hi", 4, 8.99, "apple" , ('t,b','n')]

l5 = [(i, l4[i]) for i in range(len(l4))]
print(l5)

# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = 1, 2, 3, 4
list_b = 2, 3, 4, 5

l3 = [ i for i in list_a for j in list_b if i == j]
print(l3)

# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
str = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

l5 = [i for i in str if i.isnumeric()]
print(l5)

l5 = ["even" if i % 2 == 0 else "odd" for i in range(20)]
print(l5)

# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9,
# list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

list_a = 1, 2, 3,4,5,6,7,8,9
list_b = 2, 7, 1, 12


l6 = [(i, j) for i in list_a for j in list_b if i == j]
print(l6)


# Find all of the words in a string that are less than 4 letters
str = "On a summer day somner smith went simming in the sun and his red skin stung"
new = str.split(" ")
l9 = [ i for i in new if len(i) < 4 ]
print(l9)


# Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)

l1 = [i  for i in range(1, 100) for j in range(2, 10) if i % j == 0 ]
print(set(l1))


a = ["a", "d", "c"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

n = [1, 3, 2, 1]
n.sort(reverse=True)
print(n)

m = n * 2
print(m)
#############################################################3
# Creating a set using string
test_set = set("geEks")

# Iterating using for loop
for val in test_set:
    print(val)


# max and minimum number in set
a = {1,3,5,6,8}
print(max(a))

print(min(a))


# rmove item from set
a = {1,2,3,4,5,6,7,8,9}

for i in range(len(a)):
    a.pop()
    print(a)

a = {1,2,3,4,5}
b = {6,7,8,9,3,2}

b = a.intersection(b)
print(b)



A = [1,2,3,[4,5]]
B  = copy.copy(A)

A[3][0] = 6
print(B)
print(A)


A = [1,2,3,[4,5]]
B  = copy.deepcopy(A)

A[3][0] = 6
print(B)
print(A)


a = "pooja"
b = a

a = "ketul"
print(a)




a = 3
b = 4
z = "a+b"  #must be string byte or code
result = eval(z)
print(result)

prog = """a = 3
b = 4
z = a+b
print(z) 
"""

exec(prog)
#################################################################
#lambda
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
x = lambda a : a+15
print(x(3))


# also create a lambda function that multiplies argument x with argument y and prints the result.
x = lambda x, y : x*y
print(x(2,3))

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with
# an unknown given number.

def calculate(n):
    return lambda a : a * n

p = calculate(10)   # that will return the lambda function lambda a : a * 10
print(p(2))



# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
a.sort(key=lambda x : x[1])
print(a)


class computer:
    def __int__(self):
        self.__maxprice = value

    def sell(self):
        print("selling price: {}".format(self.__maxprice))

    def SetMaxPrice(self, price):
        self._maxprice = price

c = computer()
c.sell()

# change the price
c._maxprice = 1000
c.sell()

# chnage value using setter function
c.SetMaxPrice(200)
c.sell()
