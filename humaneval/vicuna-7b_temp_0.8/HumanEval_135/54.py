
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    left = [0] * n
    right = [0] * n
    for i in range(n):
        if arr[i] > arr[i-1]:
            return i
        else:
            while arr[i] <= arr[i-1] and left[i] <= right[i]:
                left[i] += 1
            while arr[i] <= arr[i-1] and left[i-1] <= right[i]:
                right[i] -= 1
            if right[i] > left[i] + 1:
                return i
    return -1