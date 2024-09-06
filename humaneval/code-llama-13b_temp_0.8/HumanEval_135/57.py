
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # if len(arr) == 2:
    #     return -1
    #
    # if len(arr) == 3:
    #     if arr[0] > arr[1] or arr[2] >= arr[1]:
    #         return -1
    #     else:
    #         return 2
    #
    # prev = 0
    # for i in range(1, len(arr)):
    #     if arr[i] >= arr[prev]:
    #         prev += 1
    #     if prev == i:
    #         return -1
    # return prev

    # PEP8 Solution
    if len(arr) == 2:
        return -1
    if len(arr) == 3:
        if arr[0] > arr[1] or arr[2] >= arr[1]:
            return -1
        else:
            return 2
    prev = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[prev]:
            prev += 1
        if prev == i:
            return -1
    return prev

































