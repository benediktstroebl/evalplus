
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # We need a list here for the dictionary.
    arr = list(arr)
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            return min(dic[arr[i]], i)
        dic[arr[i]] = i

    return -1

