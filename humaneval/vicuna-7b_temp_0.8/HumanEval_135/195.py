
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr = sorted(arr)
    start = 0
    while start + 1 < len(arr) and arr[start] <= arr[start+1]:
        start += 1
    return start if start < len(arr) else -1
