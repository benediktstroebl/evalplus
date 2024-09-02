
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
    if not array:
        return []

    length = len(array)
    if length == 1:
        return array

    median = length // 2
    if length % 2 == 1:
        median += 1

    left = array[:median]
    right = array[median:]
    left = sort_array(left)
    right = sort_array(right)

    return left + [array[i] for i in range(0, length - 1) if array[i] > array[length - 1]] +
