
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    n = arr[0]
    result = 0
    for idx in range(1, len(arr)):
        if arr[idx] < arr[idx - 1] and arr[idx] > n:
            result = idx
            n = arr[idx]
        elif arr[idx] == arr[idx - 1]:
            result = -1
            break
    return result
