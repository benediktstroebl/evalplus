
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr:
        return -1
    return max(arr[:i] + [x for i, x in enumerate(arr[1:]) if x >= arr[i]]
               for i in range(1, len(arr)) if arr[i] > arr[i-1])
