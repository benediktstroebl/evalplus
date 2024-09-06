
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # for i in range(len(arr)-1, 0, -1):
    #     if arr[i] >= arr[i-1]:
    #         return i
    #
    # return -1

    # max_val = arr[0]
    # max_index = 0
    # for i in range(1, len(arr)):
    #     if arr[i] > max_val:
    #         max_index = i
    #         max_val = arr[i]
    # return max_index

    # low = 0
    # high = len(arr) - 1
    # while low <= high:
    #     mid = (low + high) // 2
    #     if arr[mid] >= arr[mid-1]:
    #         return mid - 1
    #     elif arr[mid] > arr[low]:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    #
    # return -1

    # return -1

    """
    Can also use binary search.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= arr[mid-1]:
            return mid - 1
        if arr[mid] > arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return -1
