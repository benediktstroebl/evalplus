
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code here
    # max_val = arr[-1]
    # for idx in reversed(range(len(arr) - 1)):
    #     if arr[idx] >= max_val:
    #         return idx
    #     max_val = max(max_val, arr[idx])
    # return -1

    # or
    # max_val = arr[-1]
    # for idx in range(len(arr)-2, -1, -1):
    #     if arr[idx] > max_val:
    #         return idx
    #     max_val = max(max_val, arr[idx])
    # return -1

    # or
    max_val = float('-inf')
    for idx, val in enumerate(arr):
        if val >= max_val:
            max_val = val
        else:
            return idx
    return -1

