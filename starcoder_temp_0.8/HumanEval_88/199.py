
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
    # find the sum of the first and last element
    # [5, 4, 3, 2, 1]
    # [5, 4, 3, 2, 1]
    # [5, 4, 3, 2, 1]
    # [5, 4, 3, 2, 1]
    # [5, 4, 3, 2, 1]
    # [5, 4, 3, 2, 1]
    # 5 + 1 = 6
    # 6 is even
    # [-4, -3, -2, -1]
    # [-4, -3, -2, -1]
    # [-4, -3, -2, -1]
    # [-4, -3, -2, -1]
    # [-4, -3, -2, -1]
    # [-4, -3, -2, -1]
    # -4 + -1 = -5
    # -5 is odd
    # [4, 3, 2, 1, 0]
    # [4, 3, 2, 1, 0]
    # [4, 3, 2, 1, 0]
    # [4, 3, 2, 1, 0]
    # [4, 3, 2, 1, 0]
    # [4, 3, 2, 1, 0]
    # 4 + 0 = 4
    # 4 is even
    # [2, 3, 4, 0, 1]
    # [2, 3, 4, 0, 1]
    # [2, 3, 4, 0, 1]
    # [2, 3, 4, 0, 1]
    # [2, 3, 4, 0, 1]
    # [2, 3, 4, 0, 1]
    # 2 + 1 = 3
    # 3 is odd
    return sorted(array, reverse=(sum(array[0], array[-1]) % 2 == 0))
