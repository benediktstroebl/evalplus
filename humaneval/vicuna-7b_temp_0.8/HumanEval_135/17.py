
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    i = 0
    largest = arr[0]
    for j in range(1, len(arr)):
        if arr[j] > arr[j-1]:
            largest = max(largest, arr[j])
        else:
            if arr[j] >= arr[j-1]:
                return -1
            i += 1
            if arr[i] > arr[j-1]:
                largest = max(largest, arr[i])
    return largest