
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_len = len(arr)
    # Sort array to maintain the order
    arr_sorted = sorted(arr)
    prev = 0
    for i in range(arr_len):
        curr = arr_sorted[i]
        if prev >= curr:
            return -1
        prev = curr

    # Starting from the first element, if the element before it is greater than
    # the element before that, then we can put the element after the element
    # before it. This is because if the element before is greater than the
    # element before that, then we definitely can arrange the array.

    for i in range(1, arr_len):
        if arr_sorted[i] <= arr_sorted[i - 1]:
            return i

    return -1
