
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
    # since the array is given, create a copy
    sort_array_copy = array.copy()

    # sort array in ascending order
    sort_array_copy.sort()

    # sum the first and last index values of the copy array
    # since the given array is sorted in ascending order, the sum of the first and last index values
    # will be an odd number
    first_and_last_index_sum = sort_array_copy[0] + sort_array_copy[-1]

    # if the sum is an odd number, sort array in descending order
    if first_and_last_index_sum % 2 == 1:
        sort_array_copy.reverse()

    # return the sorted copy array
    return sort_array_copy
