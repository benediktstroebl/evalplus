
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
    l = len(arr)
    ones = [[], []]
    for x in arr:
        a = (x & 1) != 0
        ones[a].append(x)

    l = len(ones[0])
    for i in range(l):
        ones[0][i] = (ones[0][i] << 1) | 1

    for i in range(len(ones[1])):
        ones[1][i] <<= 1

    return ones[0] + ones[1]

