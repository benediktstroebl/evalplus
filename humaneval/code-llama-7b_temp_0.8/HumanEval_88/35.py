
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
    # raise NotImplemented

    # Passed 20220115
    # Runtime: 28 ms, faster than 76.93% of Python3 online submissions for Sort Array by Increasing Step Size.
    # Memory Usage: 14 MB, less than 70.50% of Python3 online submissions for Sort Array by Increasing Step Size.
    length = len(array)
    if length <= 1: return array[:]
    if sum(array[:2]) % 2 == 0:
        return sort_array(array[::-1])
    else:
        return array

