
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # start = 0
    # end = len(arr)-1
    # while start < end:
    #     mid = (start + end) // 2
    #     if arr[mid] >= arr[mid-1]:
    #         start = mid + 1
    #     else:
    #         end = mid
    # return start
    for i in range(len(arr)):
        if arr[i] >= arr[i-1]:
            return i
    return -1
