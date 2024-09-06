
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
    # convert the array elements to their binary representations
    binary_array = [format(x, "b") for x in arr]
    # sort the array of binary representations based on number of ones
    sorted_array = sorted(binary_array, key=lambda x: x.count("1"))
    # convert the sorted binary array back to integers
    return [int(x, 2) for x in sorted_array]
