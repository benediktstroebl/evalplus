
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Can we sort the list in place?
    # If not, what's the running time?
    # Can we sort the list in a single pass?
    # What about if we sort in two passes?

    sorted_array = sorted(arr)

    max_idx = -1
    for idx in range(len(sorted_array) - 1):
        if sorted_array[idx] <= sorted_array[idx + 1]:
            max_idx = idx
        else:
            return max_idx

    return max_idx

