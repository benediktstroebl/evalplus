
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    n = len(arr)
    if n == 0:
        return [0]
    if n == 1:
        return [arr[0]]
    arr = list(arr)
    for i in range(1, n):
        for j in range(i):
            arr[i], arr[j] = arr[j], arr[i]
    result = []
    for x in arr:
        count = 0
        while x != 0:
            count += 1
            x &= x - 1
        result.append(count)
    result.sort()
    for i in range(n-1, -1, -1):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
