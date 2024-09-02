
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_elem = max(arr)

    if not max_elem or max_elem <= 0:
        return -1

    max_index = arr.index(max_elem)
    arr = arr[max_index + 1:] + arr[:max_index + 1]

    return max_index if arr[0] <= 0 else -1
