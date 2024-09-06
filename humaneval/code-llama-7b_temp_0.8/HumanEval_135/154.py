
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
    max_num = max(arr)
    index = [0] * (max_num + 1)
    for i, a in enumerate(arr):
        index[a] = i
    for i in range(len(index) - 1):
        if index[i] >= i + 1:
            return -1
    return len(arr) - 1
