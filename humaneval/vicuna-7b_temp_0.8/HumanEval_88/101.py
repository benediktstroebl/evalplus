
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

    # sort the array in ascending order
    sorted_array = sorted(array)

    # traverse the array and apply the necessary changes
    while sorted_array:
        index = (sorted_array.pop(0) // 2) * 2
        if (sorted_array[index] % 2) == 1:
            sorted_array.insert(index + 1, sorted_array.pop(0))
        else:
            sorted_array.insert(index + 1, sorted_array.pop(0))

    return [x for x in array]