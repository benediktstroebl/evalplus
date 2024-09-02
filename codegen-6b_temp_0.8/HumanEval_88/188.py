
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
    def sum(array, index):
        return array[index] + (array[-1 - index] if index > 0 else 0)

    def compare(array, index):
        return -1 if sum(array, index) % 2 else 1

    return sorted(array, key=functools.cmp_to_key(compare))


assert(sort_array([]) == [])
assert(sort_array([5]) == [5])
assert(sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5])
assert(sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0])
assert(sort_array([3, 4, 5, 6, 7, 2, 1, 0, 3, 4]) == [1, 2, 3, 4, 0, 3, 4, 5, 6, 7])
