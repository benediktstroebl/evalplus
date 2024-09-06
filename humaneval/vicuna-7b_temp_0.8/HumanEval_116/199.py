
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
    n = len(arr)
    count = [0] * n
    for i in range(n):
        for j in range(i, n):
            count[i] += int(arr[j] != 0)
    # sort count
    count.sort()
    # reverse sort array
    arr.reverse()
    # reverse sort again
    arr.reverse()
    return arr
