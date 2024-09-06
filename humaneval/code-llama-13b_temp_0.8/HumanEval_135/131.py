
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_idx = 0
    for idx in range(1, len(arr)):
        if arr[idx] >= arr[idx - 1]:
            max_idx = idx
    return max_idx if max_idx == len(arr) - 1 else -1
    
