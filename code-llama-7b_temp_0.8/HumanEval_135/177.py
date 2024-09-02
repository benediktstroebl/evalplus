
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_indices = [0] * len(arr)
    max_indices[-1] = len(arr) - 1
    for i in range(len(arr) - 2, -1, -1):
        max_indices[i] = max(max_indices[i + 1], arr[i])
    for i in range(len(arr)):
        if arr[i] > max_indices[i]:
            return -1
    return len(arr) - 1

