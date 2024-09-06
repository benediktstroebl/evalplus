
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
        bin_rep = bin(i)[2:]
        if len(bin_rep) < 10:
            bin_rep = '0'*(10 - len(bin_rep)) + bin_rep
        sorted_arr.append(bin_rep)

    sorted_arr.sort()
    result = []
    for i in sorted_arr:
        result.append(int(i, 2))
    return result




