
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
    smallest = min(array)
    largest = max(array)
    pivot = smallest + (largest - smallest) // 2
    result = [pivot] * len(array)
    for i in range(len(array)):
        if sum(array[:i + 1]) * 2 > sum(array[i + 1:]):
            result[i] = array[i]
        else:
            result[i] = array[i - 1]
    return result


assert [0, 1, 2, 3, 4, 5] == sort_array([5, 4, 3, 2, 1, 0])
assert [0, 1, 2, 3, 4, 5, 6] == sort_array([6, 5, 4, 3, 2, 1, 0])
assert [0, 1, 2, 3, 4, 5] == sort_array([2, 4, 3, 0, 1, 5])
assert [6, 5, 4, 3, 2, 1, 0] == sort_array([2, 4, 3, 0, 1, 5, 6])
