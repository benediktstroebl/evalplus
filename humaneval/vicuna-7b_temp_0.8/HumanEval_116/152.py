
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
    # sort the array by converting it to a list of tuples where the i-th element of the tuple is the i-th number in the array
    sorted_arr = list(map(tuple, arr))
    # sort the list of tuples by the number of ones in the binary representation
    sorted_arr = sorted(sorted_arr, key=lambda x: len(str(x).split('')), reverse=True)
    return sorted_arr
