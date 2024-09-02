
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
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    # 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0
    # 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0
    # 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 0, 0, 0
    # 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0
    # 6, 6, 6, 6, 6, 5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 0
    # 7, 7, 7, 7, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 2, 1
    # 8, 8, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 4, 4, 3, 2
    # 9, 9, 9, 9, 9, 8, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3
    # 10,
