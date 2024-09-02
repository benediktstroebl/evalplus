
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
        return []
    if len(array) == 1:
        return array

    # sorting the array using the builtin sort method
    sorted_array = sorted(array, reverse = True)

    # the sum of the first and last index in the sorted array
    sum_ = sorted_array[0] + sorted_array[-1]
    if sum_ % 2 == 0:
        # for even sums
        return sorted_array[::-1]
    else:
        # for odd sums
        return sorted_array


