
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
    # first pass:
    # create a new list of tuples of (value, index)
    # second pass:
    # sort the new list of tuples by value
    # third pass:
    # build the sorted array by returning the values in the order of the indexes
    sorted_value_indexes = []
    for index, value in enumerate(array):
        sorted_value_indexes.append((value, index))

    sorted_value_indexes.sort(key=lambda i: i[0])
    sorted_array = [0] * len(array)
    for value, index in sorted_value_indexes:
        sorted_array[index] = value

    return sorted_array

