
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
    arr_count = 0
    arr_index = 0

    if len(arr) == 1:
        return arr

    for i in range(len(arr)):
        if arr[i] > 0:
            arr_count += 1

    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] -= arr_count
            arr_count = 0

    while arr_index < len(arr) - 1:
        if arr[arr_index] < arr[arr_index + 1]:
            arr_index += 1
            arr.insert(arr_index, arr[arr_index])
        else:
            arr_index += 1

    
