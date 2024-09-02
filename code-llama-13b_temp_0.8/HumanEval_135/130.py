
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_max = [0] * len(arr)
    # find max so far
    for i in range(1, len(arr)):
        arr_max[i] = max(arr_max[i - 1], arr[i])
    # find the smallest index which is not greater than the previous one
    for i in range(0, len(arr) - 1):
        if arr[i + 1] <= arr_max[i]:
            return i
    return -1

