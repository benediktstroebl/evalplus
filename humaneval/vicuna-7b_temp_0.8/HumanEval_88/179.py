
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # initialize the result array with the same size of input array
    result = [0] * (len(array) + 1)
    # sort the input array in descending order
    result = sorted(array, reverse=True)
    # check the sum of the first and last element of the input array
    if sum(result[:-1]) % 2 == 0:
        # sort the result array in descending order
        result = sorted(result, reverse=True)
    else:
        # sort the result array in ascending order
        result = sorted(result)
    return result