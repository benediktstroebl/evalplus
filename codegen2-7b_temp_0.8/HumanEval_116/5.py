
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
    if not arr:
        return arr
    arr_ones = 0
    arr_zeros = 0
    for a in arr:
        if a > 0:
            arr_ones += 1
        else:
            arr_zeros += 1
    arr_ones_sorted = sort_array(arr_ones * [arr[0]])
    arr_zeros_sorted = sort_array(arr_zeros * [arr[0]])
    return arr_ones_sorted + arr_zeros_sorted

