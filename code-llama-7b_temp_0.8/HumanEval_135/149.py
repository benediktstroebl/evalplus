
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # arr.sort()
    # n = len(arr)
    # l = [i for i in range(n)]
    # l = [i for i in l if i < arr[i]]
    # if len(l) > 0:
    #     return max(l)
    # else:
    #     return -1
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1 if arr[1] > arr[0] else -1
    result = -1
    for i in range(n):
        if arr[i] <= arr[i - 1]:
            if i > 0:
                result = i - 1
            else:
                result = 0
    return result

