
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
    max_index = 0
    for i, val in enumerate(arr[1:], 1):
        if val > arr[max_index]:
            max_index = i
    return max_index if max_index!= 0 else -1









