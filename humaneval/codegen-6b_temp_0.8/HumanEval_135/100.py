
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    lst, max_index, result = [], -1, -1
    for elem in arr:
        if elem > lst[-1]:
            if max_index != -1:
                result = max(result, max_index + 1)
            max_index = len(lst)
            lst.append(elem)
        else:
            lst.append(elem)
    
    if max_index != -1:
        result = max(result, max_index + 1)
    
    return result
