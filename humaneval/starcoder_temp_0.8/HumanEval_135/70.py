
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code here
    l = len(arr)
    d = {}
    for i in range(l):
        if arr[i] not in d:
            d[arr[i]] = i
        elif arr[i] >= arr[d[arr[i]]]:
            d[arr[i]] = i
    m = -1
    for key, val in d.items():
        if val > m:
            m = val
    return m

