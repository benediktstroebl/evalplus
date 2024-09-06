
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
    # Initial check for one-number
    if not arr:
        return arr

    # Count number of ones
    count = 0
    for num in arr:
        count += (num >> 1) & 1

    # Sort based on number of ones
    mid = len(arr) // 2
    for i in range(mid, len(arr)):
        for j in range(i, mid, -1):
            arr[j], arr[i] = arr[i], arr[j]
    arr[mid], arr[mid - 1] = arr[mid - 1], arr[mid]

    # Sort based on decimal value
    arr = sorted(arr, key=lambda x: (x + (x >> 31), x // 256))

    return arr