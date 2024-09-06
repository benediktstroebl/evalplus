
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
    pivot_index = n // 2
    pivot = arr[pivot_index]
    for i in range(pivot_index, n):
        for j in range(i, n):
            if arr[j] == 1 and arr[i] == 0:
                arr[i], arr[j] = arr[j], arr[i]
    for i in range(n):
        arr[i] = arr[i] * 10 + arr[i] % 10
    return arr