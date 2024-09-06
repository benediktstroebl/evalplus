
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
    # define the first and last index values
    first_value = array[0]
    last_value = array[len(array) - 1]

    # find the sum
    sum = first_value + last_value
    # sort the array in descending order
    if sum % 2 == 0:
        array.sort(reverse=True)
    # sort the array in ascending order
    else:
        array.sort()

    return array
