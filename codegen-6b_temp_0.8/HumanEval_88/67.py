
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
    def sort(array, is_ascending, index_1, index_2):
        if index_1 >= index_2:
            return
        if is_ascending:
            if array[index_1] + array[index_2] in [1, 2]:
                array[index_1], array[index_2] = array[index_2], array[index_1]
        else:
            if array[index_1] + array[index_2] in [-1, 2]:
                array[index_1], array[index_2] = array[index_2], array[index_1]

        sort(array, is_ascending, index_1 + 1, index_2 - 1)

    sort(array, sum(array) % 2, 0, len(array) - 1)

    return array


assert sort_array([]) == []
assert sort_array([5]) == [5]
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sort_array([7, 9, 8, 6, 2, 1, 5, 4]) == [1, 2, 5, 4, 6, 7, 8, 9]
assert sort_array([7, 9, 8, 6, 2, 1, 5, 4, 3]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sort_array([8, 6, 7, 9, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
