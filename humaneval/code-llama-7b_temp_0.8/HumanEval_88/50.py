
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
    if not array: return []
    if len(array) == 1: return array

    # sort in ascending order if the sum( first index value, last index value) is odd,
    # or sort it in descending order if the sum( first index value, last index value) is even
    if sum(array[0:2]) % 2 == 1:
        ascending_list = sorted(array)
    else:
        descending_list = sorted(array, reverse=True)

    result = []
    if sum(array[0:2]) % 2 == 1:
        for i in range(len(array)):
            result.append(ascending_list[i])
    else:
        for i in range(len(array)):
            result.append(descending_list[i])
    return result

