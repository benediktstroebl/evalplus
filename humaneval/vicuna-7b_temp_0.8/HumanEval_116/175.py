
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
    # sort the array first
    arr = sorted(arr)

    # count the number of ones in each number
    number_of_ones = [0] * len(arr)
    for i, num in enumerate(arr):
        number_of_ones[i] = sum(num == 1 for num in arr)

    # sort the array based on the number of ones
    return number_of_ones