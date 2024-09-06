
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    max_val = arr[0]
    max_ind = 0

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_ind = i

    return max_ind

    # answer:

    # max_val = arr[0]
    # max_ind = 0
    # for i in range(len(arr)):
    #     if arr[i] > max_val:
    #         max_ind = i
    #         max_val = arr[i]
    # return max_ind if max_ind != len(arr) - 1 else -1

