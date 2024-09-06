
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    
    count = -1
    max_element = 0
    for i in arr:
        if i <= max_element:
            count += 1
        else:
            max_element = i
            count += 1
    return count

