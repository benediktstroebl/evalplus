
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
    # This solution is O(n) in time and O(n) in space.
    # It just sorts the array twice.
    # Once in the normal order,
    # once in the reversed order.
    # This is not an optimal solution, though.
    # I would be interested in seeing other solutions.
    array_copy = array[:]
    array_copy.sort()
    array_copy.reverse()
    array_copy.sort(key=sum_first_last_index_values, reverse=is_sum_even(array))
    return array_copy

