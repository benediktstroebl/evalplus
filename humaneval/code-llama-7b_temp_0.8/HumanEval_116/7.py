
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
    number_of_ones = []
    array = []

    # get the number of ones in each number and add it to a list
    for i in arr:
        number_of_ones.append(str(bin(i))[2:].count("1"))
        array.append(i)

    # sort based on the number of ones
    zipped = zip(number_of_ones, array)
    zipped = sorted(zipped)
    number_of_ones, array = zip(*zipped)

    # return the sorted array
    return array
