
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
    # base case
    if len(array) == 1:
        return array

    # general case
    mid_point = len(array) // 2
    left_array = array[:mid_point]
    right_array = array[mid_point:]
    left_array = sort_array(left_array)
    right_array = sort_array(right_array)
    return merge(left_array, right_array)

