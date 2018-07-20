import random

print("Hello World!")


def reverseString(s):
    ret = []

    for i in range(reversed(range(0, len(s)))):
        ret.append(s[i])
    return "".join(ret)


def fizzBuzz(i):
    for z in range(1, i + 1):
        if z % 3 == 0 and z % 5 == 0:
            print("FizzBuzz")
        elif z % 3 == 0:
            print("Fizz")
        elif z % 5 == 0:
            print("Buzz")
        else:
            print(z)


def factorial(i):
    if i == 0:
        return 1

    return i * factorial(i-1)


def linearSearch(A, i):
    pos = 0

    while pos < len(A):
        if A[pos] == i:
            return pos
        pos += 1
    return -1


array = [1, 5, 2, 3, 7, 8]
set = {5, 1, 2, 8, 6, 4, 7}


print(linearSearch(array, 10))


def divBy2():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def listLessThan10(A):
    ret = []
    for i in range(len(A)):
        if A[i] < 5:
            ret.append(A[i])


def divisors(n):
    for i in range(1, n + 1):
        if (n % i) == 0:
            print(i)


divisors(26)


def commons():
    a = range(1, random.randint(1, 30))
    b = range(1, random.randint(10, 40))
    c = []

    for i in range (len(a)):
        if a[i] in b:
            if a[i] not in c:
                c.append(a[i])
    print(a)
    print(b)
    print(c)


def palindrome(s):
    if s[:] == s[::-1]:
        print ("true")
    else:
        print ("false")

palindrome("abcba")