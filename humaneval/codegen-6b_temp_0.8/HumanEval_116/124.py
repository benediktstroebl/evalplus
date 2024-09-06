
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
    dic0 = {0: []}
    dic1 = {1: []}
    for i in arr:
        dic0[bin(i).count('1')].append(i)
        dic1[i].append(i)
    res = []
    for key in sorted(dic1.keys()):
        res = res + dic1[key]
    res = res + dic0[key]
    return res

