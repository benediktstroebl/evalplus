
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
    # 1. First, sort the array based on its decimal value.
    # 2. Second, iterate over the sorted array and make new sorted array with number of ones in
    # binary representation
    sorted_arr = sorted(arr)
    return [i for _, i in sorted((bin(j).count('1'), j) for j in sorted_arr)]

