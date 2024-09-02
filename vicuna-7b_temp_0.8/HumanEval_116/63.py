
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
    for i in range(1, len(arr)):
        # binary
        binary = 0
        while arr[i] > 0:
            binary = binary * 2 + arr[i] % 2
            i += 1
        # decimal
        decimal = (binary - (arr[i] // 2)) / 2
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr
