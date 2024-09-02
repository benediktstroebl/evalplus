
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 0 or len(arr) == 1:
        return -1

    max_idx = 0
    arr.sort(reverse=True)

    for i, elem in enumerate(arr):
        if elem <= arr[i - 1] or i == 0:
            max_idx = i
        else:
            break

    if max_idx == 0:
        return -1

    return max_idx - 1
