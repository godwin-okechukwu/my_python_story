n  = int(input("Enter a number: "))

count = 0

while n != 1:
    print(n, end=", ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(n, end=". \n")
    count += 1
    print("This took",+count, "iterations")
