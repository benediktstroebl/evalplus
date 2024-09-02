
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
    # sort the array based on the number of 1's in their binary representation
    # and, in case of ties, sort based on their decimal values

    # convert the integers in the array into their binary representation
    binary_array = [bin(i)[2:] for i in arr]

    # count the number of 1's in each binary number
    one_count = [binary_array[i].count('1') for i in range(len(binary_array))]

    # sort the array based on the number of 1's in their binary representation
    sorted_array = [binary_array[i] for i in range(len(binary_array))]
    sorted_array = sorted(sorted_array, key=one_count.__getitem__, reverse=True)

    # convert the sorted binary numbers back into integers
    return [int(i, 2) for i in sorted_array]
