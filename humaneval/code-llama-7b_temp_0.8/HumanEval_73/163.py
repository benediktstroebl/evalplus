
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
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - 1 - i]:
            break
    else:
        return 0

    l, r = i, len(arr) - 1 - i
    while l >= 0 and arr[l] == arr[r]:
        l -= 1
        r += 1
    if l < 0:
        return len(arr) - 1 - r
    while r >= 0 and arr[l] == arr[r]:
        l -= 1
        r += 1
    return min(l + 1, len(arr) - 1 - r)
