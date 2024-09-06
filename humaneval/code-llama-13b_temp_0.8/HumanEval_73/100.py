
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1

    if len(arr) == 3:
        if arr[0] != arr[2]:
            return 2
        else:
            return 1

    l = len(arr)
    r = len(arr) - 1
    min_changes = l
    while l < r:
        if arr[l] != arr[r]:
            if arr[l] == arr[r - 1] and arr[l - 1] == arr[r]:
                min_changes = min(min_changes, 3)
            else:
                min_changes = min(min_changes, 4)
        l += 1
        r -= 1
    return min_changes




