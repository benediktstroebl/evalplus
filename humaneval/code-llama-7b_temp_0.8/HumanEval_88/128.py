
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
    # check for valid input
    if not array or len(array) < 2:
        return array

    # calculate the sum of the first and last element
    sum_of_elements = array[0] + array[-1]

    # initialize the order of the array, ascending or descending
    if sum_of_elements % 2 == 1:
        order = "ascending"
    else:
        order = "descending"

    # loop through array, sort ascending or descending
    for i in range(1, len(array)):
        if order == "ascending":
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                order = "descending"
        else:
            if array[i] > array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                order = "ascending"

    # return the sorted array
    return array

