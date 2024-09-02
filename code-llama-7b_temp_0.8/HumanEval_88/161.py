
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
    # Step 0: Verify that we can work with the given input
    result_list = list()

    # Step 1: if the sum(first index value, last index value) is odd
    # sort the given array in ascending order
    if sum(array) % 2 == 1:
        result_list = array.copy()
        result_list.sort()
        return result_list

    # Step 2: if the sum(first index value, last index value) is even
    # sort the given array in descending order
    elif sum(array) % 2 == 0:
        result_list = array.copy()
        result_list.sort(reverse=True)
        return result_list

