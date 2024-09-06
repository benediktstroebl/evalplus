
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
    n = len(arr)
    # sort the array in ascending order
    arr = sorted(arr)
    # initialize variables to keep track of the count of 1s
    count = 0
    # initialize the return array
    return_arr = [0] * n
    # loop through the array
    for i in range(n):
        # increment the count of 1s for the current number
        count += (arr[i] != 0)
        # insert the current number in the return array
        return_arr[count] = arr[i]
        # decrement the count of 1s
        count -= (arr[i] != 0)
    # return the sorted array
    return return_arr