
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
    if len(array) < 2:
        return array
    # split the array into two parts
    mid_index = len(array) // 2
    first_half = array[:mid_index]
    second_half = array[mid_index:]
    # sort each half
    first_sorted = sort_array(first_half)
    second_sorted = sort_array(second_half)
    return merge(first_sorted, second_sorted)

