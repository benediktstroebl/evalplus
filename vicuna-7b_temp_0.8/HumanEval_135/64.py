
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def helper(arr, i, left=0):
        if i == len(arr) - 1:
            return 0
        if arr[i] <= arr[left]:
            return -1
        left = i + 1
        while arr[left] <= arr[i]:
            left = left + 1
        return helper(arr, left, i + 1)
    return helper(arr, 0)
