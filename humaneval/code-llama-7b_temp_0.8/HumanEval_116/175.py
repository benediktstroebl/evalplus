
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
    # pass
    # 1: base case
    if len(arr) <= 1:
        return arr

    # 2: base case
    if arr[0] & 0b1:
        return [arr[0]] + sort_array(arr[1:])
    else:
        return sort_array(arr[1:]) + [arr[0]]

