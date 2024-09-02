
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
    numerical_index = 0
    bit_index = 0
    bins = {0: [], 1: []}
    for i in arr:
        bit_length = len(bin(i)[2:])
        bins[1 if i > 0 else 0].append(i)
        bins[0 if i > 0 else 1].append(i)
    bins[1].sort()
    bins[0].sort()
    return bins[1] + bins[0]

