
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
    for i in range(1, len(arr)):
        # binary representation is [-2^i, -2^(i-1), ... , -2^0, -2^1, ..., 0, 1, ..., 2^i-1, 2^i]
        # binary representation of 0 is [0, 0, ..., 0, 1]
        # binary representation of 1 is [1, 0, ..., 0, 1]
        # binary representation of -2^i is [1, 1, ..., 1, 0]
        if arr[i] > arr[i-1]:
            arr = arr[:i] + arr[i] + arr[i+1:]
            break
    return arr
