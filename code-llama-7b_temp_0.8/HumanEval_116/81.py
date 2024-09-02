
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
    arr.sort()
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if count_ones(arr[i]) > count_ones(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
            elif count_ones(arr[i]) == count_ones(arr[j]):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return arr

