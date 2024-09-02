
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
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        pivot = arr[left]
        j = left + (len(arr) // 2)
        while j < right:
            if arr[j] == pivot:
                arr[left], arr[j] = arr[j], arr[left]
                left += 1
                right -= 1
            j += 1
    return arr