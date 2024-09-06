
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
    # Initialize variables to keep track of running time
    start_time = time.time()

    # Sorting algorithm
    def sort_array_helper(arr, i, j):
        if (arr[i] & 1) == 0:
            while (arr[j] & 1) == 0:
                j = sort_array_helper(arr, i, j)
            return j
        else:
            while (arr[j] & 1) == 0:
                j = sort_array_helper(arr, i, j)
            return i

    # Internal sorting helper function
    def sort_array_internal(arr):
        return sort_array_helper(arr, 0, len(arr) - 1)

    # Sort the array
    return sort_array_internal(arr)
