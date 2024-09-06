
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
    length = len(arr)
    result = [None] * length
    count = [0] * 10
    for i in range(length):
        count[int(bin(arr[i])[2:].count('1'))] += 1
    j = 0
    for i in range(10):
        while count[i] > 0:
            count[i] -= 1
            result[j] = 2 ** i
            j += 1
    return result

