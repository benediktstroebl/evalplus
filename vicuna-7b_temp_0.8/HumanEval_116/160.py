
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
    if not arr:
        return arr

    n = len(arr)

    # first pass: count number of ones in binary representation
    ones = 0
    for num in arr:
        ones += (num >> 1) & 1

    # second pass: sort based on number of ones
    arr = sorted(arr, key=lambda x: (ones[x - 1], x))

    # third pass: sort based on decimal value
    arr = sorted(arr, key=lambda x: x if x > 0 else float('-inf'))

    return arr