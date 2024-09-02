
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 1:
        return -1

    local_arr = arr[:]
    local_arr.sort()

    for i in range(1, len(local_arr)):
        if local_arr[i] > local_arr[i - 1]:
            return i - 1
    return -1

