
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    current = arr[0]
    max_index = 0
    for index, element in enumerate(arr):
        if index == 0:
            continue
        if element <= current:
            current = element
        else:
            max_index = index
    return max_index if max_index!= len(arr) else -1
