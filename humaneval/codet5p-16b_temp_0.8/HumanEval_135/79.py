
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    if arr == []:
        return -1
    elif arr[0] >= arr[1]:
        return 0
    elif arr[-1] <= arr[-2]:
        return -1

    n = len(arr)
    max_index = -1

    for i in range(n-1):
        if arr[i+1] <= arr[i]:
            max_index = i+1

    return max_index
