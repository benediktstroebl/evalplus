
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check edge cases
    if len(arr) <= 1:
        return -1
    if len(arr) == 2:
        if arr[0] <= arr[1]:
            return 0
        return -1

    # Sort the array in ascending order
    arr.sort()

    # Check if the array is decreasing, if so then there is no
    # index which meets the criteria
    if arr[len(arr) - 1] < arr[len(arr) - 2]:
        return -1

    # Iterate through the array
    prev_val = arr[0]
    prev_index = 0
    for i in range(1, len(arr)):
        if arr[i] <= prev_val:
            prev_index = i
            prev_val = arr[i]
        else:
            return -1
    return prev_index

