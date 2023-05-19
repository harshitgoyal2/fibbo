n = int(input("Enter the number: "))
fib1, fib2 = 0, 1
print(fib1, end=" ")
print(fib2, end=" ")

for i in range(n):
    fib3 = fib1+fib2
    fib1, fib2 = fib2, fib3
    print(fib3, end=" ")

