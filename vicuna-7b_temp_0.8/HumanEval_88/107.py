
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
    # sort the array
    array.sort()

    # initialize the result variable
    result = []

    # iterate through the array
    for element in array:
        # check the sum of the first and last element
        i = 0
        j = array.index(element)
        while j > i:
            result.append(array[i])
            i = i + 1
            j = j - 1

    return result