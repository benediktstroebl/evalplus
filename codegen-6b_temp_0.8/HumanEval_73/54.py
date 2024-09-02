
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
    count = 0
    # keep track of the minimum number of changes here
    min_changes = len(arr)
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-1-i]:
            arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
            min_changes = min(min_changes, len(arr)-1-i)
            arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    count += min_changes // 2
    return count

