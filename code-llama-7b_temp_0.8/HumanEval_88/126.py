
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
    # the array should be empty
    if array == []:
        return []

    # the length of array is 1
    if len(array) == 1:
        return array

    # the sum of the first and last index is even
    if sum(array) % 2 == 0:
        sorted_list = sort_descending(array)
        return sorted_list
    # the sum of the first and last index is odd
    else:
        sorted_list = sort_ascending(array)
        return sorted_list

