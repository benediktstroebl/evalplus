
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # time complexity O(n)
    # space complexity O(1)
    if len(arr) == 0 or len(arr) == 1:
        return -1

    maximum = arr[-1]
    last_index = len(arr) - 2

    for index in range(len(arr) - 2, 0, -1):
        if arr[index] >= maximum:
            return index
        else:
            maximum = max(maximum, arr[index])

        if arr[index] == maximum:
            last_index = index

    if maximum >= arr[0]:
        return last_index

    return -1


