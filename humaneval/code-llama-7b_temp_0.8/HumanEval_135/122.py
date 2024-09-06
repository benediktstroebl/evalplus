
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    #arr = [1,2,4,3,5]
    l = len(arr)
    arr.sort()
    max_val = arr[0]-1
    prev = arr[0]-1
    for i in range(1, l):
        if arr[i] <= max_val:
            max_val = max(arr[i], max_val)
        else:
            return -1
    return arr.index(max_val)
