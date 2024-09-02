
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
    # convert input array to list of integers in the form of [0,0,1,1,2,2,3,3,4,4,5,5]
    binary = [int(x) for x in arr]
    # sort the binary array in ascending order
    binary.sort()
    # convert the binary array back to the original array
    return [int(x) for x in binary]