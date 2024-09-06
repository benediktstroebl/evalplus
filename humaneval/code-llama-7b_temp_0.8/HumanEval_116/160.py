
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
    # Split arr into two lists, one of zeroes, one of ones
    zeroes, ones = [], []

    for val in arr:
        if val == 0:
            zeroes.append(val)
        else:
            ones.append(val)

    # Sort both lists
    zeroes.sort()
    ones.sort()

    # Now combine back
    return zeroes + ones
