
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    max_index = 0
    for i, val in enumerate(arr):
        if i > 0 and val >= arr[i-1]:
            continue
        else:
            max_index = i
            break
    return max_index if max_index!= 0 else -1

