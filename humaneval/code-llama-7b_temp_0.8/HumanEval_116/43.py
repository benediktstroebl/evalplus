
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

    bins = {}
    for i in range(1, len(arr)):
        b = str(bin(i)).replace('0b', '').replace('1', 'o')
        c = [int(x) for x in b]
        c.reverse()
        if len(c) < 5:
            c = c + [0] * (5 - len(c))
        bins[i] = c
    keys = sorted(bins.keys(), key=lambda x: (bins[x].count(1), x))
    return [arr[key] for key in keys]

