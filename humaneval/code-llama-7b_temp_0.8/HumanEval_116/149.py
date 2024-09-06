
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
    if arr == []:
        return []
    else:
        # First, sort the array in ascending order based on the number of 1s
        # in their binary representation.
        sorted_1 = sorted(arr, key = lambda x: x & -x)

        # Next, sort the array in ascending order based on the decimal value.
        # This step is needed since sorting the array based on the number of 1s
        # only works for distinct values in the array.
        sorted_2 = sorted(sorted_1, key = lambda x: x)

        return sorted_2
