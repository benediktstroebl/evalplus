
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # arr = [1,2,4,3,5]
    # arr = [1,2,3]
    if len(arr) < 2:
        return -1

    # 1. find the max value in the array
    # 2. find the min value in the array
    # 3.

    max_val = max(arr)
    min_val = min(arr)

    if max_val > len(arr):
        return -1
    if min_val < 0:
        return -1

    if min_val != 0:
        return -1

    if max_val == len(arr):
        return -1

    if max_val == min_val:
        return max_val

    if max_val < len(arr):
        return max_val

    return -1
