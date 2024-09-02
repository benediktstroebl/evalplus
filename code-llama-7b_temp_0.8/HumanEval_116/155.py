
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
    ones = []
    for i in arr:
        binary_str = bin(i)
        ones_in_binary = binary_str.count('1')
        ones.append((ones_in_binary, i))

    ones.sort(key=lambda x: (x[0], x[1]))
    return list(map(lambda x: x[1], ones))

