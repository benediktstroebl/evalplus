
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
    sorted_array = array[:]
    for i in xrange(len(sorted_array) - 1):
        if sum(sorted_array[i]) > sum(sorted_array[i + 1]):
            index = i
            for k in xrange(index, i - 1, -1):
                sorted_array[k], sorted_array[k + 1] = sorted_array[k + 1], sorted_array[k]
        else:
            index = i + 1
            for k in xrange(index, len(sorted_array)):
                sorted_array[k], sorted_array[k - 1] = sorted_array[k - 1], sorted_array[k]

    return sorted_array

