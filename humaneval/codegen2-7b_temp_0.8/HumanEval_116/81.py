
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
    new_arr = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            new_arr.append(arr[i])

    for i in range(len(arr)):
        if arr[i] < 0:
            new_arr.append(abs(arr[i]))
    return new_arr
