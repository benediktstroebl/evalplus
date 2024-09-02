
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
    # if there is only one element, return 0
    if arr_len == 1:
        return 0
    # if there are no elements, return -1
    if arr_len == 0:
        return -1

    count = 0
    # search for the largest index of an element which is not greater than or equal to the element immediately preceding it
    for i in range(1, arr_len):
        # if the element is not greater than or equal to the element immediately preceding it
        if arr[i] > arr[i-1]:
            # increment the count
            count += 1
        # if the element is greater than or equal to the element immediately preceding it
        if arr[i] <= arr[i-1]:
            # return the largest index of an element which is not greater than or equal to the element immediately preceding it
            return count

    # if no such element exists, return -1
    return -1
