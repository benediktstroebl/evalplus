
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

    max_val = arr[-1]
    max_index = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] <= max_val:
            break
        max_val = arr[i]
        max_index = i

    if max_val < arr[max_index - 1]:
        return -1

    smaller_index = -1
    for i in range(max_index - 1, -1, -1):
        if arr[i] < max_val:
            smaller_index = i
            break

    return smaller_index
