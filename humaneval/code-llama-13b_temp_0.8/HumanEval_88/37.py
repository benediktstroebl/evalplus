
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
    ##############
    # Solution 1 #
    # O(n) time | O(n) space - where n is the length of the array
    # ----------------------------------------------------------
    # if not array:
    #     return []
    #
    # sorted_array = array.copy()
    # sorted_array.sort()
    #
    # if sum(array[0], array[-1]) % 2 == 0:
    #     sorted_array.reverse()
    #
    # return sorted_array
    ###################################################
    # Solution 2 #
    # O(n log n) time | O(1) space - where n is the length of the array
    # -----------------------------------------------------------------
    if not array:
        return []

    return sorted(array, key=lambda num: sum(array[0], array[-1]) % 2)
