
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
    from collections import defaultdict
    counter = defaultdict(int)
    for e in arr:
        counter[str(bin(e))[2:]] += 1
    l = []
    for k in sorted(counter.keys()):
        l.append(int(k, 2))
    return sorted(arr, key = lambda x: (counter[str(bin(x))[2:]], x))
