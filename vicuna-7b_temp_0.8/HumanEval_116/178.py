
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
    sorted_arr = [0] * n
    for i in range(n):
        for j in range(i, n):
            if arr[i] == 0 and arr[j] == 0:
                # No ones, just swap with current element
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
            elif arr[i] != 0:
                # One one, swap with current element
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
    return sorted_arr[n-1:], arr