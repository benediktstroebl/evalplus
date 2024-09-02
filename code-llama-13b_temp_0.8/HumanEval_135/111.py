
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1
    pivots = []
    if arr[1] <= arr[0]:
        pivots.append(1)
    for idx in range(2, len(arr)):
        if arr[idx] < arr[idx - 1] and arr[idx] <= arr[idx - 2]:
            pivots.append(idx)
    return max(pivots) if pivots else -1
