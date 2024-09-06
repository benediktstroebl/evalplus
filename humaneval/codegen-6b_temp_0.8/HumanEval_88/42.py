
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
    return sorted(array, reverse=sum(array[0], array[-1]) % 2)


assert sort_array([]) == []
assert sort_array([5]) == [5]
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
assert sort_array([0, 0, 3, 2, 3, 4, 2]) == [0, 0, 2, 2, 3, 3, 4]
assert sort_array([7, 1, 2, 4, 5, 3, 6]) == [1, 2, 3, 4, 5, 6, 7]
assert sort_array([3, 2, 4, 1, 9, 2, 10, 5, 7, 0]) == [0, 1, 2, 2, 3, 4, 5, 7, 9, 10]
