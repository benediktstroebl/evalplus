
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
    a = []
    for i in arr:
        b = bin(i)[2:]
        if len(b) < 32:
            b = 0
            for j in range(32 - len(b)):
                b = b + "0"
        a.append(b.count("1"))
    return sorted(arr, key=lambda x: (a.index(x), x))
