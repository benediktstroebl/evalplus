
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
    #############################
    # ITERATIVE SOLUTION
    # it is based on the fact that for each given value
    # the sum of the first index value and the last index value is odd or even
    # (i.e. the sum is odd if the value is in odd position and even if it is in even position)
    #
    # i.e. we can split the array in two different arrays:
    # one where the values are in odd positions and one where the values are in even positions
    # and apply the normal sorting algorithm
    #
    # O(n) time and space
    # n = len(array)
    #
    # array = [1, 2, 3, 4, 5]
    # first_half_array = [1, 3, 5]
    # second_half_array = [2, 4]
    #############################
    # 1 - validate input
    # 2 - split in two arrays
    # 3 - sort each array
    # 4 - merge the arrays
    # 5 - return result
    #############################
    # 1 - validate input
    if array == []:
        return array

    # 2 - split in two arrays
    first_half_array = []
    second_half_array = []

    # iterate the array
    for index, value in enumerate(array):
        if index % 2 == 0:  # even
            first_half_array.append(value)
        else:  # odd
            second_half_array.append(value)

    # 3 - sort each array
    first_half_array = sorted(first_half_array)
    second_half_array = sorted(second_half_array)
    second_half_array.reverse()

    # 4 - merge the arrays
    array = first_half_array + second_half_array

    # 5 - return result
    return array

