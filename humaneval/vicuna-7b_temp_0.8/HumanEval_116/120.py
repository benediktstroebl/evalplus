
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
    # find the pivot point
    pivot = arr[-1]
    for i in range(n-1, -1, -1):
        # swap the pivot with the element
        arr[i], arr[i-1] = arr[i-1], arr[i]
        # find the number of 1's in the binary representation of the pivot
        pivot_ones = sum(1 for i in range(len(pivot)) if pivot[i] == 1)
        # find the number of 1's in the binary representation of the current element
        current_ones = sum(1 for i in range(len(arr[i])) if arr[i][i] == 1)
        # if the pivot has more 1's than the current element, swap them
        if pivot_ones > current_ones:
            arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr