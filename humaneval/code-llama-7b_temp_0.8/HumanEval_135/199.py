
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # O(nlogn) time and O(1) space
    arr.sort()
    for i in range(len(arr)):
        if arr[i] >= arr[i - 1]:
            return i - 1
    return -1

    # O(n) time and O(n) space
    # seen = set()
    # for i, e in enumerate(arr):
    #     if e in seen:
    #         return i - 1
    #     seen.add(e)
    # return -1

