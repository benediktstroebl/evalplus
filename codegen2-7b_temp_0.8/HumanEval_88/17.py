
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
    if len(array) == 1:
        return array

    first_index = 0
    last_index = len(array) - 1

    while first_index < last_index:
        sum_value = sum(array[first_index:last_index + 1])
        if sum_value % 2 == 0:
            array[first_index:last_index + 1] = array[first_index:last_index + 1][::-1]
            first_index += 1
        else:
            last_index -= 1

    return array

