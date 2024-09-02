
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    prev_element = arr[0]
    max_element = 0
    for i, num in enumerate(arr):
        if num >= prev_element:
            max_element = i
            break
        prev_element = num
    return -1 if max_element == 0 else max_element - 1
