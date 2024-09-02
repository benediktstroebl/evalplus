
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
    else:
        pivot_index = n//2
        pivot = arr[pivot_index]
        left_half = [i if i < pivot_index else pivot for i in arr]
        right_half = [i if i >= pivot_index else pivot for i in arr]
        return merge(left_half, right_half)
