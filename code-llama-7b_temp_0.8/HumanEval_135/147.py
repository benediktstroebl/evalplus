
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
    if len(arr) == 0:
        return -1
    else:
        last = arr[-1]
        # The value of the last element can't be a candidate because it can't be greater than its
        # preceding elements.
        candidates = arr[:-1]
        for i in range(len(candidates), 0, -1):
            if candidates[i-1] <= candidates[i-2]:
                return i-1
        return -1
