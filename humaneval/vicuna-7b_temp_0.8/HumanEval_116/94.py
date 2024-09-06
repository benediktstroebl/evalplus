
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
        return [0]
    else:
        arr_bin = []
        for num in arr:
            arr_bin.append(str(num).count('1'))
        arr_bin = [int(x) for x in arr_bin]
        arr_bin.sort()
        result = [0] * (n + 1)
        i = 0
        while i < n:
            result[i] = arr_bin[i]
            i += 1
        result_dec = [int(x) for x in result]
        result_dec.sort()
        return result_dec