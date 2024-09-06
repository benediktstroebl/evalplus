
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # M1:
    n = len(arr)
    if n < 2:
        return -1

    for i in range(n):
        if arr[i] > arr[i - 1]:
            continue
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            j -= 1
        if j < 0:
            return -1
        arr[i], arr[j] = arr[j], arr[i]
        if j + 1 < n and arr[j + 1] >= arr[i]:
            return -1
        i = j
    return i

    # M2:
    n = len(arr)
    if n < 2:
        return -1

    for i in range(n - 1, 0, -1):
        if arr[i] >= arr[i - 1]:
            return -1
    return n - 1

