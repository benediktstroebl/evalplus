
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # The largest index of a value will be <= the index of its preceding value
    arr_reversed = arr[::-1]
    max_idx = -1
    for i in range(len(arr_reversed)):
        if arr_reversed[i] <= arr_reversed[i-1]:
            max_idx = i
            break

    return max_idx
