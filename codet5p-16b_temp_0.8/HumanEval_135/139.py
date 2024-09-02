
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    if len(arr) <= 2:
        return -1

    inc = [None] * len(arr)
    for i in range(len(arr)):
        if i == 0:
            if arr[i] > arr[i+1]:
                inc[i] = i+1
            else:
                inc[i] = -1
            continue
        if arr[i] > arr[i-1]:
            inc[i] = i
        else:
            inc[i] = i-1

    return inc.index(max(inc))

