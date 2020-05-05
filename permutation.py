def fact(x):
    i = 1
    for y in range(1, x+1):
        i = i*y
    return i
print("nCx")
n = int(input("n: "))
x = int(input("x: "))
a = fact(n)
b = fact(x)*fact(n-x)
print("nCx = " + str(a/b))
