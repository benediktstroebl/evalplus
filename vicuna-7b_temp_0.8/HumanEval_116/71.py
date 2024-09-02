
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
    # Step 1: Find first index of non-zero element
    i = 0
    while arr[i] == 0:
        i += 1
    # Step 2: Start binary search from the found index
    j = i
    while j < n:
        while j >= i and arr[j] == 0:
            j -= 1
        while j < i and arr[j] != 0:
            j += 1
        if j - i > 0:
            # Binary search
            arr = [arr[j], arr[i], ..., arr[n-1]]
            j = sort_array(arr)
            arr = [arr[0], arr[i], ..., arr[j-1]]
            return arr
        i += 1
    return [arr[i]]