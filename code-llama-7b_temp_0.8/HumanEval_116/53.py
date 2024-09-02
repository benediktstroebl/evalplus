
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

    from math import log
    from bisect import bisect_left

    n = len(arr)
    if n == 0:
        return []

    bits = log(max(arr), 2) + 1
    counts = [0] * (n + 1)
    # Calculate counts of each number
    for x in arr:
        counts[int((x << (bits + 1)) % ((1 << (bits + 1)) - 1))] += 1
    # Add prefix sum to find insertion position for each number
    for i in range(n):
        counts[i + 1] += counts[i]
    # Calculate result based on counts
    result = [0] * n
    for x in arr:
        result[counts[int((x << (bits + 1)) % ((1 << (bits + 1)) - 1)) - 1]] = x
        counts[int((x << (bits + 1)) % ((1 << (bits + 1)) - 1)) - 1] += 1
    return result

