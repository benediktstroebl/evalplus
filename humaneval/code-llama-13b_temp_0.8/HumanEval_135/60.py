
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # --------------------------------------------------------------------------
    # Solution:
    #   1. Iterate through the list, keeping track of the largest value seen so
    #   far and the largest value seen so far that is smaller than the value
    #   before it.
    #   2. If we find such a pair, return the index of the second value. If we
    #   reach the end of the list without finding such a pair, return -1.
    # --------------------------------------------------------------------------
    max_seen = float('-inf')
    largest_gap_index = -1
    for idx, val in enumerate(arr):
        if val >= max_seen:
            max_seen = val
        else:
            largest_gap_index = idx - 1
    return largest_gap_index

