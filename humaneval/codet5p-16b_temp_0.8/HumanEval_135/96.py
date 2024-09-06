
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    new_list = []
    for index in range(len(arr)):
        if index == 0:
            new_list.append(arr[index])
        else:
            if arr[index] > arr[index-1]:
                new_list.append(arr[index])
            else:
                new_list.append(-1)

    return new_list.index(-1)
