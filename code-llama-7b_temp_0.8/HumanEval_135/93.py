
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # O(n) time | O(1) space
    # assume a[0] <= a[1] <= a[2] ...
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0
    i = 1
    while i < n:
        if arr[i] >= arr[i - 1]:
            i += 1
        else:
            break
    if i == n:
        return -1
    left = i - 1
    right = i
    while right < n:
        if arr[right] <= arr[left]:
            left = right
            right += 1
        else:
            break
    if right == n:
        return left
    return -1

