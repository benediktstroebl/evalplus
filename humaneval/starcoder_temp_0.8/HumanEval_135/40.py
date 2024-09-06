
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    temp_dict = {}
    for index, value in enumerate(arr):
        if index == 0:
            if value >= arr[index + 1]:
                return -1
        else:
            if value >= arr[index + 1]:
                if value >= temp_dict.get(arr[index - 1], None):
                    return index - 1
                else:
                    return index
            else:
                temp_dict[value] = arr[index + 1]
    return -1
