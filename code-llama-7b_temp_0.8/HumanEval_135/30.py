
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

    if len(arr) == 1:
        return 0

    prev_i = 0
    prev_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < arr[prev_i]:
            prev_val = arr[i]
            prev_i = i
        elif arr[i] >= arr[prev_i]:
            prev_val = arr[prev_i]
            prev_i = -1
            break

    return prev_i

