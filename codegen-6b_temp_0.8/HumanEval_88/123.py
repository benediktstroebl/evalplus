
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
        return array

    result = [0] * len(array)
    descending = False
    for i in range(len(array) - 1):
        if (sum(array[i], array[-1 - i]) % 2) == 0:
            descending = False
        else:
            descending = True

        if descending:
            result[i], result[-1 - i] = array[-1 - i], array[i]
        else:
            result[i], result[-1 - i] = array[i], array[-1 - i]

    return result

