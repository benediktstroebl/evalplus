
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
    
    if len(arr) == 0:
        return []

    ones = sum(bin(x).count('1') for x in arr)

    if ones == 0:
        return [int(x) for x in sorted(map(str, arr))]
    else:
        return [int(x) for x in sorted(map(str, arr), key=lambda x: int(x, 2
