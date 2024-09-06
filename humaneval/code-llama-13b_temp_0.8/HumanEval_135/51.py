
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code goes here
    max_index = 0
    for i, item in enumerate(arr):
        if item <= arr[max_index]:
            max_index = i
    return -1 if max_index + 1 == len(arr) else max_index
