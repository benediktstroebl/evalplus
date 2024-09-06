
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    N = len(arr)
    nums = [0 for x in range(N)]
    for i in range(N-1):
        if arr[i+1] <= arr[i]:
            nums[i+1] = arr[i]
    nums[-1] = arr[-1]
    for i in range(N):
        if arr[i] > nums[i]:
            return i
    return -1
