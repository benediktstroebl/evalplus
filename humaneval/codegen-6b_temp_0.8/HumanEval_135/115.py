
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def _ar(x, i=0):
        if x in arr[i:]:
            return -1
        for j in range(i, len(arr)):
            if arr[j] > x:
                return j
        return -1
    return _ar

