
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
    if arr == arr[::-1]:
        return 0
    if arr == sorted(arr):
        return len(arr) - 1
    index_max = 0
    max_val = arr[index_max]
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            index_max = max(index_max - 1, i)
            max_val = arr[i]
    for i in range(len(arr)-1, index_max, -1):
        if arr[i] < arr[index_max]:
            index_max = i
            max_val = arr[i]
    prev_change = float('inf')
    for i in range(index_max, -1, -1):
        if arr[i] < max_val:
            prev_change = 1
        elif arr[i] > max_val and prev_change > 1:
            return prev_change + 1
        else:
            prev_change += 1
    return prev_change


