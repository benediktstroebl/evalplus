
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
        return -1
    if len(arr) == 1:
        return 0

    min_changes = -1

    for i in range(len(arr)):
        current_changes = 0
        for j in range(len(arr)):
            if arr[i]!= arr[j]:
                arr[j] = arr[i]
                current_changes += 1
                break
        min_changes = min(current_changes, min_changes) if min_changes!= -1 else current_changes
    return min_changes

