
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # your code here
    max_so_far = -1
    for index in range(1, len(arr)):
        if arr[index] >= arr[max_so_far]:
            max_so_far = index
    if max_so_far == -1:
        return -1
    for index in range(max_so_far):
        if arr[index] <= arr[max_so_far]:
            return -1
    return max_so_far

