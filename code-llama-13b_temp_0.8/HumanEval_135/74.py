
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 1:
        return 0
    curr_idx = 0
    while curr_idx < len(arr) - 1:
        if arr[curr_idx] <= arr[curr_idx + 1]:
            curr_idx += 1
        else:
            break
    return curr_idx
    
