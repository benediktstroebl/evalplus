
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
    arr = list(arr)
    while arr:
        # check for end of list
        if arr[0] == 0:
            return arr[1:]
        # count the number of 1s
        count = 0
        for num in arr:
            count += (num & 1)
        # move all elements with the same number of 1s to the beginning
        arr, _ = partition(count, arr, arr + [0])
    return arr