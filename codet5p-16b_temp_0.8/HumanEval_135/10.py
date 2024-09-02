
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    if arr == sorted(arr):
        return -1

    sorted_arr = sorted(arr)
    for i, val in enumerate(sorted_arr):
        if val!= sorted_arr[i-1] and val!= sorted_arr[i]:
            return i
    return -1

