
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

    pivot = array[len(array) // 2]
    equal_part = array[: len(array) // 2]
    left_part = [v for v in equal_part if v < pivot]
    right_part = [v for v in equal_part if v >= pivot]

    return sort_array(left_part) + [pivot] + sort_array(right_part)

