
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    current_index = 0
    max_index = len(arr) - 1
    for index in range(max_index):
        if arr[index] < arr[index + 1]:
            current_index = index + 1
    return -1 if current_index == 0 else current_index

