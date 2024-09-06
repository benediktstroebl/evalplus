
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
    result = [0] * (len(array) + 1)
    for index, item in enumerate(array):
        result[index + 1] = item
    if len(result) & 1:
        result[-1] = result[-1] / 2
    else:
        result[-1] = result[-1] / 2 * -1
    sorted_result = sorted(result)
    return sorted_
