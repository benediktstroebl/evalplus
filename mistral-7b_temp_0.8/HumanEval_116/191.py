
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

    # Sort the array in place
    # Logic: First sort the array based on the number of ones, and then
    #        sort the array based on the decimal value.

    # Sort the array based on the number of ones
    arr.sort(key=lambda x: bin(x).count('1'))

    # Sort the array based on the decimal value
    arr.sort()

    return arr
