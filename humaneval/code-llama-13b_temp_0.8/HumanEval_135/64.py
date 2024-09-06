
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # MY SOLUTION
    current_max = float('-inf')
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > current_max:
            return i
        else:
            current_max = max(current_max, arr[i])
    return -1

    # BOOK SOLUTION
    # current_max = float('-inf')
    # for i in range(len(arr) - 1, -1, -1):
    #     if arr[i] > current_max:
    #         return i
    #     else:
    #         current_max = max(current_max, arr[i])
    # return -1
