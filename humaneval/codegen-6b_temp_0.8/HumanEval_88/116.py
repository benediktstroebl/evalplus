
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

    odd_index = 0
    odd_end = len(array) - 1

    for i in range(len(array)):
        if i == odd_end:
            break

        if (i + array[i]) % 2 == 1:
            array[odd_index], array[i] = array[i], array[odd_index]
            odd_index += 1

    if odd_index == len(array):
        return array

    return array[:odd_index] + sorted(array[odd_index:], reverse=True)

