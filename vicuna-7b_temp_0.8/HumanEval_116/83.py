
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
    if n == 1:
        return arr[0]
    low = 0
    high = n // 2
    while low <= high:
        i = (low + high) // 2
        if arr[i] == 0:
            low = i + 1
        elif arr[i] == 1:
            high = i - 1
    return arr[low:] + arr[high:]