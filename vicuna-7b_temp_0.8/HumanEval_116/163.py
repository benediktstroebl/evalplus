
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
    # base case, sorted with 0 elements
    if n == 0:
        return [0]
    # pivot selection
    pivot = arr[n // 2]
    # partitioning the array
    left = [i for i in arr[0:n // 2] if i < pivot]
    right = [i for i in arr[n // 2:] if i > pivot]
    return merge(left, right)
