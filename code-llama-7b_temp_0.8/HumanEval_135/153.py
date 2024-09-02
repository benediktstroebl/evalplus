
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # O(n) time
    # O(n) space

    # Edge cases
    if len(arr) == 0:
        return 0

    if arr[0] == 1:
        return 0

    if len(arr) == 1:
        return -1

    # for every element in the list starting with the second, find the first
    # element that is not greater than it. If one is found, set it's index
    # to be the current element's index
    for i in range(1, len(arr)):
        # find the first element that is not greater than the current element
        for j in range(i-1, -1, -1):
            if arr[j] == 1:
                continue

            if arr[j] < arr[i]:
                arr[i] = j
                break

    # return the last index we found
    return arr[-1]

