
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) <= 1:
        return -1

    for index, num in enumerate(arr):
        for j in range(index - 1, -1, -1):
            if num <= arr[j]:
                continue
            return j

    return -1
