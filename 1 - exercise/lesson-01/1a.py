#Determine the Big O notations of the functions

 """

def func1(arr):
    for i in arr:
        print(i)


def func2(arr):
    for i in arr:
        for j in arr:
            print(i, j)


def func3(arr):
    print(arr[0])
    print(arr[-1])


def func4(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(i, j)


def func5(n):
    i = 1
    while i < n:
        i *= 2
        print(i)


def func6(arr):
    for i in arr:
        print(i)
    for j in arr:
        print(j)


def func7(arr):
    if len(arr) > 0:
        print(arr[0])


 """