
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
    array_length = len(array)
    for i in range(0, array_length):
        if i == 0:
            if array[i] % 2 == 0:
                swap_index = i
            else:
                swap_index = i + 1
        else:
            if array[i] % 2 == 0:
                swap_index = i
            else:
                swap_index = i + 1
        array[swap_index], array[i] = array[i], array[swap_index]
    return
