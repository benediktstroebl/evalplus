
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
    if len(arr) == 1 or arr == arr[::-1]:
        return 0
    min_changes = 10000
    for i in range(len(arr)):
        if len(arr[i:]) >= len(arr[:i]):
            changes = len(arr) - len(arr[i:])
            changes += max(arr[i:]) - min(arr[:i])
            min_changes = min(changes, min_changes)
        else:
            changes = len(arr) - len(arr[:i])
            changes += max(arr[:i]) - min(arr[i:])
            min_changes = min(changes, min_changes)
    return min_changes

