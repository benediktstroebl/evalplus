
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    indices = {}
    for i, val in enumerate(arr):
        if val in indices:
            indices[val] += 1
        else:
            indices[val] = 1
    max_val = max(indices.keys())
    if max_val * (indices[max_val] - 1) < max_val:
        return -1
    for i in range(1, len(arr)):
        val_before = arr[i - 1]
        if arr[i] < val_before and arr[i] <= max_val - val_before:
            return i
    return -1
    
