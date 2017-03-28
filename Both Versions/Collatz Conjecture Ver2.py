s = 2
n = s

while True:
    n = s
    print(s)
    while n != 1:
        if float(n/2).is_integer():
            n = n/2
            print(n)
        else:
            n = (3 * n) + 1
            print(n)
    s = s + 1
    n = s
    print("")
    print("")
    print("")
    print("")
