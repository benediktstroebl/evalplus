
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # My solution - 2 pointers, slow and fast
    slow = 0
    fast = 1
    while fast < len(arr):
        if arr[fast] >= arr[slow]:
            slow += 1
            fast += 1
        else:
            slow += 1
    if slow == len(arr):
        return -1
    return slow - 1

    # Fastest solution
    # Sort the array then iterate to find the first element which is smaller
    # than the one immediately preceding it
    arr.sort()
    prev = arr[0] - 1
    for i in range(1, len(arr)):
        if arr[i] <= prev:
            return i - 1
        prev = arr[i]
    return -1
