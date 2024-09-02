
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
    # 1. Two pointers.
    # 2. Iterate and compare the first and last elements.
    # 3. If the sum of these two elements is odd, we will move the first element to the back.
    # 4. If the sum of these two elements is even, we will move the last element to the back.
    # 5. Find the middle value and compare it with the first and last value and move the first and last value
    #   to the match position.
    # 6. This is why do we have to compare the middle value, to the first and last value.
    # 7. Could we do better? Try to go through the array in the following order:
    #   0, 1, 2, 3, 4, 5, 6
    #   0, 1, 2, 3, 4, 5, 6
    #   0, 1, 2, 3, 4, 5, 6
    #   0, 1, 2, 3, 4, 5, 6
    #   0, 1, 2, 3, 4, 5, 6
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2, 3, 4, 5, 6)
    #   (0, 1, 2