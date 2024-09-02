
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # TODO:
    # The array does not contain duplicate values.
    # First, I sort the array.
    arr.sort()
    # I create an empty list.
    result_arr = []
    # I iterate over the sorted array.
    for index, value in enumerate(arr):
        # I append the element to the empty list.
        result_arr.append(value)
    # I iterate over the array.
    for index, value in enumerate(arr):
        # If the element is greater than the previous element,
        # I return -1.
        if value >= arr[index - 1]:
            return -1
        # If the element is not greater than the previous element,
        # I append the element to the empty list.
        result_arr.append(value)
    # I return the largest index of an element which is not greater
    # than the element immediately preceding it.
    return result_arr.index(max(result_arr))
