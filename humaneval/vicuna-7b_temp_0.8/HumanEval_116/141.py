
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
    arr = sorted(arr)
    n = len(arr)
    if n == 0:
        return [0]
    d = [0] * (n + 1)
    for i in range(n):
        for j in range(i, n):
            b = 0
            for k in range(i):
                if arr[k] == 1:
                    b += (arr[k] - 1) // 2
            d[i] = d[j] + b
            d[j] = d[i] + (arr[i] - 1) // 2
    return d
