
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
    min_changes = len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            for k in range(len(arr)):
                if arr[j] != arr[k]:
                    arr[j], arr[k] = arr[k], arr[j]
                    if arr[j] == arr[i]:
                        arr[i], arr[j] = arr[j], arr[i]
                        min_changes = min(min_changes - 1, 2)
    return min_changes
