
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    prev_val = arr[0]
    for idx in range(1, len(arr)):
        if idx == len(arr) - 1:
            return len(arr) - 1

        if arr[idx] <= prev_val:
            return idx
        prev_val = arr[idx]

    return -1

