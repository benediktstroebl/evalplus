
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

    result = [0]*len(array)
    if len(array) == 0:
        return array
    result[0] = array[0]
    for index in range(1, len(array)):
        result[index] = array[index]
        if (index - 1) % 2 == 0:
            while result[index] < result[index-1] and index - 1 > 0:
                result[index], result[index-1] = result[index-1], result[index]
                index -= 1
        else:
            while result[index] > result[index-1] and index - 1 > 0:
                result[index], result[index-1] = result[index-1], result[index]
                index -= 1

    return result
