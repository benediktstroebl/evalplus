
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
    # sort the array first
    array = sorted(array)

    # keep track of the last index value
    last_index = len(array) - 1

    # loop through the array
    for i in range(len(array)):
        # check if the sum of the first index value and the last index value is odd
        if (array[i] + last_index) % 2 == 1:
            # if it is odd, swap the current element with the last element
            array[i], array[last_index] = array[last_index], array[i]

        # if the sum of the first index value and the last index value is even, swap the current element with the next element
        elif (array[i] + last_index) % 2 == 0:
            # swap the current element with the next element
            array[i], array[i + 1] = array[i + 1], array[i]

    return array