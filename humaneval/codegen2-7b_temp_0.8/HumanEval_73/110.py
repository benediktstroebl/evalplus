
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
    arr.sort()
    prev = arr[0]
    min_changes = 0
    for i in range(1, len(arr)):
        if arr[i] == prev:
            continue
        if arr[i] == arr[i - 1] - 1:
            min_changes += 1
            prev = arr[i]
            continue
        if arr[i] == arr[i - 1] + 1:
            prev = arr[i]
            continue
        min_changes += 1
        prev = arr[i]
    return min_
