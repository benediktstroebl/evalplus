
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # if arr is empty or sorted, return -1
    if not arr or arr == sorted(arr):
        return -1
    # if the first and last element are not greater than or equal to each other,
    # return the first index of an element that is not greater than or equal to
    # the element immediately preceding it
    if arr[0] <= arr[-1]:
        return max(i for i, a in enumerate(arr))
    # if the first element is greater than the second element, it cannot be
    # arranged and return -1
    if arr[0] > arr[1]:
        return -1
    # otherwise, loop through the array and check if the element is not greater
    # than or equal to the element immediately preceding it
    i = 0
    for a in arr:
        if a > arr[i - 1]:
            return max(i for i, a in enumerate(arr))
    return -1