
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
    copy_array = [x for x in array]
    i = 0
    while i < len(copy_array) - 1:
        if (sum(copy_array[i]) % 2 != 0) or (sum(copy_array[i + 1]) % 2 != 0):
            copy_array.insert(i + 1, copy_array[i])
            i += 1
        else:
            copy_array[i] = max(copy_array[i], copy_array[i + 1])
            i += 1
    return copy_array
