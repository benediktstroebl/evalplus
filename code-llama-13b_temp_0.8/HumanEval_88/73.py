
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
    if len(array) == 0:
        return array

    index = 0
    # We are going to assume the first index element has been sorted correctly,
    # and iterate through the rest of the list.
    while index < len(array) - 1:
        # check the index against the next index.
        if (array[index] + array[index + 1]) % 2 == 0:
            # if they are even, switch them.
            temp = array[index]
            array[index] = array[index + 1]
            array[index + 1] = temp
        index += 1
    return array
