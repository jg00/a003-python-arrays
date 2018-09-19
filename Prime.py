number = int(input("Enter a number: "))

instance = 0
for i in range(2,number+1):
    if (number % i == 0):
        instance = instance + 1

if (instance > 1 or number == 1):
    print("{} not a prime".format(number))
else:
    print("{} is a prime".format(number))

