
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ###########################################################################
    # TODO: Implement can_arrange function.
    #   * Use the "break" statement to exit a loop once the return value has
    #     been determined.
    #   * Return -1 if no suitable index exists.
    #     (i.e., the largest index is less than or equal to the smallest index)
    ###########################################################################
    # pass # REMOVE AFTER PLACING YOUR CODE HERE
    if len(arr) < 2:
        return -1
    largest_i = 0
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            largest_i = i
    return largest_i if largest_i >= 0 else -1
    ###########################################################################
    # END
    ###########################################################################
