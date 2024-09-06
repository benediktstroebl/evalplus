
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
    first_index, last_index = 0, len(array) - 1
    result_array = []
    if sum(array[0], array[last_index]) % 2 == 0:
        # Even
        first_index = len(array) - 1
        last_index = 0

    while first_index < last_index:
        if array[first_index] < array[last_index]:
            result_array.append(array[first_index])
            first_index += 1
        elif array[first_index] > array[last_index]:
            result_array.append(array[last_index])
            last_index -= 1
        else:
            result_array.append(array[first_index])
            first_index += 1
    if first_index == last_index:
        result_array.append(array[first_index])
    return result_array
