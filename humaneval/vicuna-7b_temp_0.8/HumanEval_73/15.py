
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
    if len(arr) == 1:
        return 0
    min_changes = 0
    min_changes_arr = arr[:]
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                min_changes -= 1
                min_changes_arr[j], min_changes_arr[i] = min_changes_arr[i], min_changes_arr[j]
                break
        if min_changes == 0:
            break
    return min_changes
