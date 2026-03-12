n = int(input("Enter number: "))

flag = False

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break

if flag:
    print("Not a Prime Number")
else:
    print("Prime Number")
