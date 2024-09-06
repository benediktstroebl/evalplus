
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
        return 0
    max_arr = arr[0]
    max_index = 0
    for index in range(1, len(arr)):
        if arr[index] > max_arr:
            max_arr = arr[index]
            max_index = index
    return max_index
