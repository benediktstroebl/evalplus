
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
    # binary_representation(n) will not change during the sort
    arr = sorted(arr, key=lambda x: binary_representation(x) + (n // 2,))
    # if the last digit of binary representation of a number is 0 or 1,
    # the next number should be the number with the same binary representation
    # but the next digit should be the opposite (1 -> 0, 0 -> 1)
    # this is equivalent to saying that the number should be swapped
    # if it has a different number of ones in binary representation
    for i in range(n-1, -1, -1):
        if arr[i] == 0 and arr[i+1] == 1:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
