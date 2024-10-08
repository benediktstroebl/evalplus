
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
    # First sort the array so that all the elements with the same number of ones in their binary representation are together.
    arr = sorted(arr)

    # Then, sort the array again so that elements with more ones come first.
    arr = sorted(arr, key=lambda x: (sum(bin(x)[2:].split('') == '1'), x))

    return arr
