
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
    if len(array) <= 1:
        return array
    left_index = 0
    right_index = len(array) - 1
    result = list(array)
    while left_index < right_index:
        while result[left_index] % 2 == 0 and left_index < right_index:
            left_index += 1
        while result[right_index] % 2 != 0 and left_index < right_index:
            right_index -= 1
        if left_index < right_index:
            result[left_index], result[right_index] = result[right_index], result[left_index]
    return result
