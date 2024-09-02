
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
    swaps, i = 0, 0
    while i < len(arr)-1:
        if is_bit_one(arr[i]):
            n = 1
            while i+n < len(arr)-1 and is_bit_one(arr[i+n]):
                n = n + 1
            if n > len(arr) // 2:
                swaps += (len(arr) - 1 - i) * 2
            i += n
        else:
            i += 1
    return arr[:len(arr)-swaps] + [0] * swaps

