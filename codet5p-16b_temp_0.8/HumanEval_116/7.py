
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

    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    for i in range(arr_len):
        max_i = 0
        max_e = -1
        for j in range(i, arr_len):
            if bin(arr[j])[2:].count('1') > max_e:
                max_e = bin(arr[j])[2:].count('1')
                max_i = j
        if i!= max_i:
            arr[i], arr[max_i] = arr[max_i], arr[i]
    return arr

