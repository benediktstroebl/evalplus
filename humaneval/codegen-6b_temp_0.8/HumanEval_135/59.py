
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    pivot_idx = 0

    for i in range(len(arr)):
        if arr[i] > arr[pivot_idx]:
            pivot_idx = i

    if arr[0] <= arr[pivot_idx]:
        return -1

    pivot_idx -= 1
    next_pivot_idx = len(arr) - 1

    while pivot_idx < next_pivot_idx:
        if arr[pivot_idx] <= arr[next_pivot_idx]:
            pivot_idx += 1
            next_pivot_idx -= 1
        else:
            return next_pivot_idx

    return -1

