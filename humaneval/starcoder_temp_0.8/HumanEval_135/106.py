
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
    elif len(arr) == 2:
        if arr[0] <= arr[1]:
            return 1
        else:
            return 0

    sorted_arr = sorted(arr)
    for index, element in enumerate(sorted_arr[1:], start=1):
        if element < sorted_arr[index-1]:
            return index-1

    return -1
