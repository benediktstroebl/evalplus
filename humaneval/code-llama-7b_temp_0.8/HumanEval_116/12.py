
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
    if not arr or len(arr) == 0:
        return arr

    if len(arr) == 1:
        return arr

    arr.sort()

    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] < arr[i]:
            j -= 1

        if j >= 0 and arr[j] < arr[i]:
            for k in range(j + 1, i):
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
        elif j >= 0 and arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

    return arr

