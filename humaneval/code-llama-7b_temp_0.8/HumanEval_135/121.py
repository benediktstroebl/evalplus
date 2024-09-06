
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # sort(arr)
    # d = {}
    # for i in range(len(arr)-1):
    #     if arr[i+1] <= arr[i]:
    #         d[arr[i]] = arr.index(arr[i])

    # for i in range(len(arr)-1,0,-1):
    #     if arr[i] not in d.keys():
    #         d[arr[i]] = arr.index(arr[i])

    # return d
    print(arr)
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            return i
    return -1

