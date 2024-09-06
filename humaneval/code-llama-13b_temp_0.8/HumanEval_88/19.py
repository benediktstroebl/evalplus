
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
    if array == []:
        return array

    def sort_recursively(sorted_array, array_to_sort):
        if len(array_to_sort) == 0:
            return sorted_array

        if sum(sorted_array[-1], array_to_sort[0]) % 2 == 0:
            return sort_recursively(sorted_array + [array_to_sort[0]], array_to_sort[1:])
        else:
            return sort_recursively(sorted_array[:-1] + [array_to_sort[0]], array_to_sort[1:])

    return sort_recursively([], array)
