def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If the given array does not contain
    duplicate values, return -1."""
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            return i
    return -1