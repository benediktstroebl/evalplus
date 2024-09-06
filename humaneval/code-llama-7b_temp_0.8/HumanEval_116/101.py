
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
    if len(arr) == 0:
        return arr

    left, right = 0, len(arr) - 1
    while left < right:
        if (arr[left] & 1) and (arr[right] & 1):
            left += 1
            right -= 1
        elif (arr[left] & 1) and not (arr[right] & 1):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        elif not (arr[left] & 1) and (arr[right] & 1):
            right -= 1
        else:
            left += 1
            right -= 1
    return arr
