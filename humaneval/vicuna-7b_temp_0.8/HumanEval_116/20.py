
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
    # Build a dictionary where keys are non-negative integers and values are
    # their binary representation with leading zeros removed.
    num_bin = {}
    for num in arr:
        num_bin[num] = bin(num)[2:]

    # Sort the dictionary by the number of ones in the binary representation
    num_bin_ones = [len(bin(i)[2:]) for i in num_bin]
    num_bin_ones.sort()

    # Convert back to original array
    sorted_arr = [i for i in num_bin if i in num_bin_ones[0]]

    return sorted_arr
