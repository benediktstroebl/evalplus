
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
    sorted_arr = []
    for i in arr:
        bin_repr = bin(i)[2:].rjust(32, '0')
        if i < 0:
            sorted_arr.append(int(''.join(['1' if x == '1' else '0' for x in bin_repr[::-1]])))
        else:
            sorted_arr.append(int(''.join(['0' if x == '1' else '1' for x in bin_repr[::-1]])))
    return sorted_
