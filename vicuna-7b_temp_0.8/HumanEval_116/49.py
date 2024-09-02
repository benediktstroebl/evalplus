
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
    ones_count = 0
    for i in range(n):
        if arr[i] == 1:
            ones_count += 1
            sorted_arr[i] = arr[i]
        else:
            j = binary_search(sorted_arr, ones_count)
            sorted_arr[j] = arr[i]
            ones_count = 0
            sorted_arr[i] = arr[i]
            if arr[i] >= 0:
                break
    return [sorted_arr[i] for i in range(n)]
