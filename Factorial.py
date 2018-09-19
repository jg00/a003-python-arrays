#5 facotiral 120    5 * 4 * 3 * 2 * 1
number = int(input("Enter a number: "))

value = number
for i in range(1,number):
    value = value * i

print("{} factorial is {}".format(number,value))




# def factorial(number):
#     value = number
#     for i in range(1,number):
#         value = value * i 
#     return value

# result = factorial(number)
# print(result)