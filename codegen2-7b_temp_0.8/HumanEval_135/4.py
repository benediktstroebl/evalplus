
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1
    prev_elm = arr[0]
    max_idx = 0
    for elm in arr[1:]:
        if elm <= prev_elm:
            prev_elm = elm
        else:
            max_idx = max(max_idx, elm - prev_elm)
    return max_idx if max_idx > 0 else -
