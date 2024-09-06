
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # for index, value in enumerate(arr):
    #     if index == len(arr) - 1:
    #         continue
    #     elif arr[index + 1] > value:
    #         return index

    # return -1
    # write your code here
    for index, value in enumerate(arr):
        if index == len(arr) - 1:
            continue
        if arr[index + 1] > value:
            return index
    return -1

