
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] <= arr[left + 1]:
            left += 1
        elif arr[right] >= arr[right - 1]:
            right -= 1
        else:
            return -1
    return max(left, right)

