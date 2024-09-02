
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    return max(map(lambda x: 0 if x > x-1 else x, arr))

    # We could also use a while loop here to achieve the same result
    # while arr[0] > 0:
    #   if arr[0] > arr[1]
    #   return 0
    #   arr[0] -= 1
    #   return arr[0]
    # return -1

    # Another way we could write this is as follows:
    # if arr[0] > 0:
    #   return arr[0]
    # else:
    #   return -1
