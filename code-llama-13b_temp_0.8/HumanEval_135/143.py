
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # O(n) time, O(1) space
    max_seen = arr[0]
    for idx in range(len(arr) - 1):
        if max_seen <= arr[idx + 1]:
            max_seen = arr[idx + 1]
        else:
            return idx
    return -1
