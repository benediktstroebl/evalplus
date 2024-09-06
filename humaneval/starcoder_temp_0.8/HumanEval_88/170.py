
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
    # Solution 1:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # return array if len(array) <= 1 else sort_array(array[::2]) + sort_array(array[1::2])

    # Solution 2:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # return array if len(array) <= 1 else sort_array(array[1:]) + [array[0]]

    # Solution 3:
    # Time complexity: O(n)
    # Space complexity: O(1)
    is_odd = sum(array[:2]) & 1
    return sort_array(array[1:]) + (array[:1] if is_odd else array[-1:])
