
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    last_element = None
    for index, element in enumerate(arr):
        if last_element is not None and element < last_element:
            return index - 1
        last_element = element
    return -1
        
        
