import random as ran

a = int(input("write a number between 1 and 100: \n"))
r = ran.randint(1, 100)
bigger = 100
lower = 1
b = 0
while a != r:
    if r > a:
        # if b == r:
        #     continue
        print(r)
        bigger = r
        b = r
        r = ran.randint(lower, bigger)

    elif a > r:
        # if b == r:
        # continue
        print(r)
        lower = r
        b = r
        r = ran.randint(lower, bigger)

print(r)
print("you found it")

# 2nd not working func

# import random as ran
#
# a = int(input("write a number between 1 and 100: \n"))
# r = ran.randint(1, 100)
# bigger = 100
# lower = 1
# b = 0
# while a != r:
#     if r > a:
#         if b == r:
#             continue
#         print(r)
#         bigger = r
#         b = r
#         r = ran.randint(lower, bigger)
#
#     elif a > r:
#         if b == r:
#             continue
#         print(r)
#         lower = r
#         b = r
#         r = ran.randint(lower, bigger)
#
# print(r)
# print("you found it")
