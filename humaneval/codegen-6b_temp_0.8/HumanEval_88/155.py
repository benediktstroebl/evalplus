
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

    sum_, c = sum(array), 0
    if sum_ % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)


assert(sort_array([]).__eq__([])), "Failed Test 1: empty array, expecting: []"
assert(sort_array([5]).__eq__([5])), "Failed Test 2: single parameter, expecting: [5]"
assert(sort_array([2, 4, 3, 0, 1, 5]).__eq__([0, 1, 2, 3, 4, 5])), "Failed Test 3: ascending array, expecting: [0, 1, 2, 3, 4, 5]"
assert(sort_array([2, 4, 3, 0, 1, 5, 6]).__eq__([6, 5, 4, 3, 2, 1, 0])), "Failed Test 4: descending array, expecting: [6, 5, 4, 3, 2, 1, 0]"

