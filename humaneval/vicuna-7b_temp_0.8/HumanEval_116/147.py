
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
    # Shift all elements to left and fill zeros
    left = 0
    while arr[left] != 0:
        left += 1
    while left < len(arr):
        for i in range(len(arr)):
            arr[left + i] = arr[i]
        left += len(arr)
        for i in range(len(arr)):
            arr[left + i] = 0
        left += len(arr)
        for i in range(len(arr)):
            arr[left + i] = arr[i]
        # Copy last part of the array to the beginning
        for i in range(len(arr)):
            arr[i] = arr[left + i]
    # Now all non-zero elements are at the left
    return arr