
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
    if not array:
        return []
    # make a new array, copy the original array, and sort it
    new_array = array.copy()
    new_array.sort()
    # set the starting and ending indices
    start_i, end_i = 0, len(new_array) - 1
    # iterate through array in ascending order
    for i in range(len(new_array) - 1):
        if sum(new_array[start_i], new_array[end_i]) % 2 == 0:
            start_i += 1
        else:
            end_i -= 1
    return new_array[start_i:end_i+1]

assert sort_array([]) == []
assert sort_array([5]) == [5]
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
assert sort_array([2, 4, 3, 0, 1, 5, 3]) == [3, 0, 1, 2, 5, 3, 4]
assert sort_array([2, 4, 3, 0, 1, 5, 6, 8]) == [8, 6, 5, 4, 3, 2, 1, 0]
assert sort_array([2, 4, 3, 0, 1, 5, 0]) == [0, 1, 2, 3, 4, 5, 0]
assert sort_array([2, 4, 30, 0, 1, 5, 0]) == [0, 1, 2, 3, 4, 5, 30]
assert sort_array([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_array([0, 1, 1, 1]) == [0, 1, 1, 1]
assert sort_array([0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert sort_array([5, 1, 4, 2, 3, 0]) ==