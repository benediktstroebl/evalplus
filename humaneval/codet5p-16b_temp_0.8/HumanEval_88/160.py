
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

    if len(array) < 2:
        return array

    pivot_index = len(array) // 2
    left_array = array[:pivot_index]
    right_array = array[pivot_index:]

    left_array = sort_array(left_array)
    right_array = sort_array(right_array)

    sorted_array = []

    while left_array and right_array:
        if sum(left_array[0]) > sum(right_array[0]):
            sorted_array.append(left_array.pop(0))
        else:
            sorted_array.append(right_array.pop(0))

    sorted_array = sorted_array + left_array + right_array

    return sorted_array
