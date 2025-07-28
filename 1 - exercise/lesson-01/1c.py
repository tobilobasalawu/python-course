'''

1. for i in range(1, n):
    print(i)


2. for i in range(n):
    for j in range(n):
        print(i, j)


3. def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


4. print("Hello World")


5. for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)

6. for i in range(n):
    for j in range(5):
        print(i, j)

7. def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

8. def double_loop(nums):
    for i in nums:
        for j in nums:
            if i + j == 0:
                return True
    return False

9. def recursive_branch(n):
    if n <= 1:
        return 1
    return recursive_branch(n - 1) + recursive_branch(n - 1)

10. for i in range(n):
    print(i)
for j in range(n):
    print(j)

'''