
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
    # check the given array
    if len(array) == 0:
        return array

    # get the first and last index of the array
    first_index = array[0]
    last_index = array[-1]

    # get the sum of the first and last index
    sum_of_indices = first_index + last_index

    # if the sum is even, sort in descending order
    if sum_of_indices % 2 == 0:
        # sort in descending order
        sorted_array = array.sort(reverse=True)

        return sorted_array

    # if the sum is odd, sort in ascending order
    else:
        # sort in ascending order
        sorted_array = array.sort()

        return sorted_array

