
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
    ################################################################################
    # TODO(callsen): Implement this method.
    # Hint:
    # * reverse is a boolean variable.
    # * sorted function can take key argument to implement any comparison operation.
    # * reverse=True means descending sort.
    # * reverse=False means ascending sort.
    # * you can get the sum of first and last element of the list as sum(array[0], array[-1])
    # * make sure to return a copy of array (not the original one)
    # * the return value should be sorted list.
    # * you can use built-in sum function.
    # * you can use built-in copy function.
    ################################################################################
    # pass

    reverse = sum(array[0], array[-1]) % 2 == 0
    return sorted(array, reverse=reverse)
    ################################################################################
    # ------------------------------------------------------------------------------
    # The above is the answer.
    # ------------------------------------------------------------------------------
    ################################################################################
