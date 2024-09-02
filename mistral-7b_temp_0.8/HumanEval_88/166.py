
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
    # create a copy of the input array
    array_copy = array[:]

    # check if the sum of the first and last index value is odd or even
    first_index_value = array_copy[0]
    last_index_value = array_copy[-1]
    sum_of_index_values = first_index_value + last_index_value

    if sum_of_index_values % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()

    return array_copy
