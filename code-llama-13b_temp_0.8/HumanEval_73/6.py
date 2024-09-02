
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
    if len(arr) == 0:
        return 0

    num_changes = 0
    min_val = 0
    max_val = 0

    for idx in range(len(arr)):
        if arr[idx] < min_val:
            min_val = arr[idx]
        if arr[idx] > max_val:
            max_val = arr[idx]
        if arr[idx] != max_val:
            num_changes += 1

    if num_changes > (len(arr) - max_val):
        return len(arr) - max_val

    return num_changes

