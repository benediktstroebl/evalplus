
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    if len(arr) == 1:
        return -1
    if len(arr) == 2:
        return 0 if arr[1] < arr[0] else -1

    index = 1
    for i in range(2, len(arr)):
        if arr[i]!= arr[index] and arr[i] < arr[index]:
            index = i
        elif arr[i] == arr[index] and arr[i]!= arr[index - 1]:
            index = i
    return -1 if index == 1 else index
