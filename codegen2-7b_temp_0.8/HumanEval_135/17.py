
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def can_arrange_rec(arr, ndx):
        if ndx < 0:
            return -1
        if arr[ndx] > arr[ndx-1]:
            return can_arrange_rec(arr, ndx - 1)
        return ndx
    return can_arrange_rec(arr, len(arr) - 1)
