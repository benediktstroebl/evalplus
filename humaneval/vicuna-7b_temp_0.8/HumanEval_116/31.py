
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
    # convert input array to a list of integers
    arr_list = list(arr)
    # sort the list in ascending order
    arr_list.sort()
    # initialize an empty list to store the result
    result = []
    # iterate over the sorted list
    for num in arr_list:
        # convert num to binary and append it to the result list
        binary = bin(num)[2].zfill(16)
        result.append(binary)
    return result
