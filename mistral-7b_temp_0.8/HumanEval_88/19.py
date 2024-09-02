
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

    # initializing our sorted array
    sorted_array = []

    # if the sum of the first index and the last index is odd, we will sort our array in ascending order
    # if the sum of the first index and the last index is even, we will sort our array in descending order
    if (array[0] + array[-1]) % 2 == 0:
        sorted_array = sorted(array, reverse=True)
    else:
        sorted_array = sorted(array)

    return sorted_array
