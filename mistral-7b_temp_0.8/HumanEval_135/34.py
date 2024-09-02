
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
    left = [0]*n
    right = [n]*n

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            left[i] = i-1
        else:
            left[i] = left[i-1]

    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            right[i] = i+1
        else:
            right[i] = right[i+1]

    max_index = 0
    for i in range(n):
        if max_index == i:
            break
        if left[i] < i and i < right[i]:
            max_index = i

    return max_index

