
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_max = max(arr)
    if arr_max ** 2 > sum(arr):
        return -1
    if arr_max ** 2 == sum(arr):
        return len(arr) - 1

    diff = arr_max ** 2 - sum(arr)

    for i, num in enumerate(arr):
        if num <= diff:
            return i
    return -1
