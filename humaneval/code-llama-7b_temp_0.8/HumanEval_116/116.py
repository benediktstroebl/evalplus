
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
    arr_of_ones = []
    arr_of_zeroes = []
    for element in arr:
        if len(str(bin(element))) - 2 > 0:
            ones = len(str(bin(element))) - 2
            if ones not in arr_of_ones:
                arr_of_ones.append(ones)
            arr_of_ones.sort()
            arr_of_ones.append(element)
        else:
            if element not in arr_of_zeroes:
                arr_of_zeroes.append(element)
            arr_of_zeroes.sort()
    return arr_of_ones + arr_of_zeroes
