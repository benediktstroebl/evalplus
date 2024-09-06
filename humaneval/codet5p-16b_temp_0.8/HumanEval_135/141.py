
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    if len(arr) < 3:
        return -1
    res = -1
    prev_num = None
    prev_pos = None
    for i in range(len(arr)):
        if arr[i] == prev_num:
            return -1
        if arr[i] > prev_num:
            if prev_pos!= None:
                res = max(res, prev_pos)
            prev_pos = i
            prev_num = arr[i]
    return res
