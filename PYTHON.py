# # change string into lower case
# a = "POOJA"
# b = a.lower()
# print(b)
#
# # change string into upper case
# a = "pooja"
# b = a.upper()
# print(b)
#
# # remove whitespace from beginning and end
# a = "   Pooja  "
# b= a.strip()
# print(b)
# print(a.rstrip())
# print(a.lstrip())
#
# # replace string with another string
# a = "pooja"
# b = "sona"
# c=a.replace(b)
# print(a)


# row = 5
# for i in range(0, row):
#     print(i * "*", end=' ')
#     print(" ")
# for i in range(row, 0, -1):
#     print(i * "*", end=" ")
#     print(" ")

# list = [10, 20, 30, 40, 50, 60]
# for i in list[1::2]:
#     print(i , end=" ")

# a = [0, 1]
# for i in range(1,10):
#     b = a[-2] + a[-1]
#     a.append(b)
# print(a) # it will print a list
# for i in a:
#     print(i, end= " ")  # it will print a sequence

# # prime number
# # prime number is greater than one
# for i in range(2,30):
#     for j in range(2, i):
#         a = i % j
#         if a == 0:
#             break
#     else:
#         print(i)

# # reversed number
# list = [10, 20, 30]
# new = reversed(list)
# for i in new:
#     print(i)

row = 5
for i in range(0, row+1):
    for j in range(5-i,0, -1):
        print(j, end=" ")
    print(" ")
