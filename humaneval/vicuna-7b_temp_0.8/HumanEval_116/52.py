
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
    # sort first n-1 elements
    for i in range(n - 1):
        j = bisect_left(arr, i + 1)
        for k in range(i, j):
            arr[k], arr[j] = arr[j], arr[k]
    # sort the last element with different algorithm
    arr.sort()
    # if the last element is zero, it means there are more zeros than ones in the array
    # so we have to reverse the array
    if arr[-1] == 0:
        arr.reverse()
    return arr
