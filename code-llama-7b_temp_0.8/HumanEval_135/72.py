
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 0:
        return -1
    else:
        max_value = max(arr)
        min_value = min(arr)
        if max_value <= min_value:
            return -1

    for i in range(len(arr)):
        if arr[i] >= max_value:
            arr[i] = -1
        else:
            arr[i] = i

    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            arr[i] = arr[i + 1]
        else:
            arr[i + 1] = arr[i]

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < 0:
            return i
    return -1

