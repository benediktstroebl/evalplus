
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
    # sort array
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] > arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    # sort array according to number of ones in binary representation
    while len(arr) > 1:
        i = 0
        while i < len(arr) and arr[i] == arr[i + 1]:
            i += 1
        while i < len(arr):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
    return arr