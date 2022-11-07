number = 10
print("Fibonacci series of 10 numbers is")

n1, n2 = 0, 1
count = 0

while count < number:
    print(n1)
    a = n1 + n2

    n1 = n2
    n2 = a
    count += 1
