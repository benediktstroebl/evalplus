
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    leng = len(arr)
    for i in range(0, leng):
        candidate = arr[i]
        prev_index = i - 1
        prev_value = arr[prev_index] if prev_index >= 0 else float('inf')
        if candidate < prev_value:
            return prev_index

    return -1

