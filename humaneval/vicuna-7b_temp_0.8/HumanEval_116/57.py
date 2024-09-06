
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
    # two pointers, one for the first one, one for the second one
    i, j = 0, n-1
    while i < j:
        # swap if first one is greater
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = j, i+1

    # the first segment contains only zeros, swap it with the rest of the array
    while i < n-1 and arr[i] == 0:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 1

    return arr
