
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
    left, right = 1, 0
    while left < len(arr):
        while left < len(arr) and arr[left] == 0:
            left += 1
        while right < len(arr) and arr[right] == 0:
            right += 1
        if arr[left] == 0:
            left += 1
            if arr[left] != 0:
                left += 1
            while arr[right] != 0:
                right += 1
                if arr[right] != 0:
                    right += 1
    return arr[:left] + arr[left:right] + arr[right:]
