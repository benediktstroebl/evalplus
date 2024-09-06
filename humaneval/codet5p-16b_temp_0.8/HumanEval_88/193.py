
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

    result = []
    if not array:
        return result
    sorted_array = sorted(array)
    left_index = 0
    right_index = len(sorted_array) - 1
    while left_index < right_index:
        sum_of_indexes = sorted_array[left_index] + sorted_array[right_index]
        if sum_of_indexes % 2 == 0:
            result.append(sorted_array[left_index])
            result.append(sorted_array[right_index])
            left_index += 1
            right_index -= 1
        else:
            result.append(sorted_array[right_index])
            result.append(sorted_array[left_index])
            left_index += 1
            right_index -= 1
    if left_index == right_index:
        result.append(sorted_array[left_index])
    return result

