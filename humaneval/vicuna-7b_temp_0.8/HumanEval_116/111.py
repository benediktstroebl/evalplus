
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
    if n == 0:
        return []
    if n == 1:
        return arr

    # binary_to_decimal(arr[0]) contains the number of ones in the binary representation
    # of the first number, so we can compare it to the rest of the array
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == 0:
            low = mid + 1
        else:
            high = mid - 1

    # if the mid number is greater than the first number, we need to swap it
    # with the first number so that it can be correctly compared to the rest
    # of the array
    if arr[0] > arr[mid]:
        arr[0], arr[mid] = arr[mid], arr[0]

    # sort the array based on the binary_to_decimal number of ones
    return sorted(arr, key=lambda x: binary_to_decimal(x))