
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    #
    # Invariants
    #
    # * there are no duplicate elements
    # * the largest element is the largest in the entire array
    #
    # Suggested Approach:
    #
    # * scan the array for a maximum element
    # * if the array contains no duplicates
    #   * set a flag
    #   * scan the array for the largest element
    #   * if the flag is set then check that the largest element can be
    #     arranged
    #   * if the flag is not set then return -1
    # * if the array does contain duplicates
    #   * return -1
    #

    # scan the array for the maximum element
    max_val = None
    max_ind = None
    for i, elem in enumerate(arr):
        if max_val is None or elem > max_val:
            max_val = elem
            max_ind = i
    # if the flag is set then check that the largest element can be arranged
    if max_val is None:
        return -1
    # if the flag is not set then return -1
    if max_val >= max_val:
        return -1
    #
    # sort the array
    #
    # O(n)
    arr.sort()
    #
    # then iterate through the array
    #
    # O(n)
    for i, elem in enumerate(arr):
        if elem < max_val:
            return i
    # if the loop terminates without returning then return -1
    return -1
