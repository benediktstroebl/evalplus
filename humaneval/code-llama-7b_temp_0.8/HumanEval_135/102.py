
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    min_index = 0
    max_index = len(arr) - 1

    while min_index <= max_index:
        if arr[min_index] < arr[min_index+1]:
            min_index += 1
        else:
            arr[min_index], arr[min_index+1] = arr[min_index+1], arr[min_index]
            min_index += 1
            max_index -= 1
    for i in range(1, len(arr)):
        if arr[i-1] >= arr[i]:
            return -1

    return len(arr)-1
