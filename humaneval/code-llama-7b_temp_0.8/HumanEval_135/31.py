
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

    result = -1
    prev_num = arr[0]
    for i, num in enumerate(arr[1:]):
        if num > prev_num:
            result = i
            prev_num = num
        else:
            return result
    return result

