
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
    # if the length of the array is 0, return an empty list
    if len(array) == 0:
        return []

    # initialize the first and second pointer to point to the first and second element of the array
    first = 0
    second = 0

    # initialize the sum of the first and last elements of the array to 0
    sum = 0

    # sort the array
    while first < len(array) - 1:
        if sum % 2 == 0:
            first = first + 1
            second = second + 1
            sum = sum + array[first]
            while sum > array[second - 1]:
                array[first], array[second] = array[second], array[first]
                sum = sum - array[second - 1]
        else:
            first = first + 1
            second = second + 1
            sum = sum + array[first]
            while sum > array[second - 1]:
                array[first], array[second] = array[second], array[first]
                sum = sum - array[second - 1]

    # return a copy of the sorted array
    return array.copy()