
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
    # a solution that runs in O(n) time and O(n) space
    if len(array) == 0: return []

    sum_first_last = sum(array[:2])
    result = array[::] if sum_first_last % 2 == 0 else array[::-1]

    for i in range(2, len(array)):
        if sum(result[:2]) % 2 != sum_first_last % 2:
            result[i], result[i-1] = result[i-1], result[i]

    return result
