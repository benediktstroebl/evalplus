
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
    #=========================================================================
    # Return a sorted array of numbers, where the numbers are sorted by the
    # number of 1s in their binary representation. If two numbers have the
    # same number of 1s, sort them based on their decimal value.
    #=========================================================================
    sorted_nums = sorted(arr, key = lambda x: (x & -x).bit_length())
    return sorted_nums
