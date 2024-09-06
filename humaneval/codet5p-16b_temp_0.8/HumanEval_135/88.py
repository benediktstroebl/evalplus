
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    new_arr = []
    for index in range(len(arr)):
        if index == 0:
            new_arr.append(arr[index])
        else:
            if arr[index] >= new_arr[-1]:
                new_arr.append(arr[index])
            else:
                return index-1
    return -1
