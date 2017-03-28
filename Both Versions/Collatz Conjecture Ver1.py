n = int(input("gimme a number "))

while n != 1:
    if float(n/2).is_integer():
        n = n/2
        print(n)
    else:
        n = (3 * n) + 1
        print(n)
