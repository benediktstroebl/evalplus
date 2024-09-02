
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_val = None
    max_val_idx = -1
    for idx, val in enumerate(arr):
        if idx > 0 and arr[idx - 1] <= val:
            return idx - 1
        if val > max_val:
            max_val = val
            max_val_idx = idx
    return -1 if max_val_idx == -1 else max_val_idx
        
