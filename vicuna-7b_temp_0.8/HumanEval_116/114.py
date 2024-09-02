
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
    # sort the array
    arr = sorted(arr)

    # count the number of ones in the array
    num_ones = 0
    for num in arr:
        if num == 1:
            num_ones += 1

    # determine the pivot index based on the number of ones
    if num_ones % 2 == 0:
        pivot_index = 0
    else:
        pivot_index = 1

    # partition the array using the pivot index
    i = 0
    j = arr[pivot_index]
    while i < len(arr) and arr[i] <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1

    return arr
