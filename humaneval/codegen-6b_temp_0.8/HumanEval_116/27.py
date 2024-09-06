
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
    counter_dict = {}
    for x in arr:
        counter_dict[x] = ''.join(list(bin(x)[2:].rjust(32, '0').rjust(5, '0'))).count('1')
    arr.sort(key=lambda x: (counter_dict[x], x))
    return arr

