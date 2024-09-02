
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    doublets = []
    for i in range(len(arr)):
        if i == 0:
            doublets.append(None)
        else:
            doublets.append(arr[i] - arr[i-1])
    for i in range(len(arr)):
        j = 1
        while j < len(arr) and i - j + 1 < len(arr):
            if doublets[i-j] > 0 and doublets[i-j] < arr[i-j+1] - arr[i]:
                return i - j
            j += 1
    return -1


