
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def max_index(arr):
        l = len(arr)
        for k in range(l-1):
            if arr[k+1] > arr[k]:
                return k
        return -1
    return max_index(arr)
