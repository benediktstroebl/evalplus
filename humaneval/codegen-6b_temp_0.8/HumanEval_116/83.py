
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
    count = [0]*length
    for i in arr:
        count[i] += 1
    res = [0]*length
    for i in range(length):
        if res[i] == 0:
            res[i] = arr[i]

    for i in range(length-1, -1, -1):
        if count[res[i]] > 0:
            res[i] = arr[i]
            count[arr[i]] -= 1
    return res

