
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
        return [0] * n
    arr_bin = [arr[i] + (arr[i] >> 1) // 2 for i in range(1, n)]
    bin_sum = 0
    while bin_sum < n:
        i = (bin_sum // 2 + n // 2) % n
        arr_bin[i] = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr_bin[i] > arr_bin[j]:
                arr_bin[i], arr_bin[j] = arr_bin[j], arr_bin[i]
    return [int(bin) for bin in arr_bin]