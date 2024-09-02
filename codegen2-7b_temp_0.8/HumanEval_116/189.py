
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
    sorted_arr = []
    ones = 0
    zeros = 0
    while arr:
        curr = arr.pop()
        if curr == 0:
            zeros += 1
        else:
            ones += 1
        if zeros <= ones:
            sorted_arr.append(0)
        else:
            sorted_arr.append(1)
    return sorted_arr +
