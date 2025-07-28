"""
def funcA(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            return True
    return False

def funcB(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)

def funcC(n):
    if n <= 1:
        return 1
    else:
        return funcC(n-1) + funcC(n-1)

def funcD(arr):
    mid = len(arr) // 2
    print(arr[mid])

def funcE(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 0:
            return True
        elif arr[mid] < 0:
            left = mid + 1
        else:
            right = mid - 1
    return False

def funcF(arr):
    for i in range(len(arr)):
        j = 1
        while j < len(arr):
            j *= 2
            print(i, j)

def funcG(arr):
    for i in range(len(arr)):
        for j in range(5):
            print(i, j)

"""