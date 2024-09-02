
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
    arr = sorted(arr)
    l, r = 0, len(arr) - 1
    changes = 0
    while l < r:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        elif arr[l] != arr[r]:
            if arr[l + 1] != arr[r]:
                changes += 1
                arr[l + 1], arr[r] = arr[r], arr[l + 1]
            l += 1
            r -= 1
    return changes

