
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
    if n == 0:
        return []
    arr = [arr[0]]
    for i in range(1, n):
        j = 0
        count = 0
        while j < i:
            if arr[i] == 0 and arr[j] == 0:
                count += 1
                j += 1
            elif arr[i] != 0 and arr[j] == 0:
                arr[j] = 0
            elif arr[i] != 0:
                arr[j] = 0
                count = 1
            else:
                arr[j] = 0
                count += 1
            j += 1
        arr[j] = 0
        if count == n - i:
            arr = arr[:j + 1] + [0] * (n - i - j)
        else:
            arr = arr[:j] + [0] * (n - i - j - 1) + [arr[i]]
    return arr