
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
    n = len(arr)
    min_change = n * (n + 1) // 2
    min_change = max(min_change, 0)
    min_change_change = 0
    for i in range(min_change):
        for j in range(i, n):
            arr[j], arr[i] = arr[i], arr[j]
            min_change_change = min(min_change_change, 1)
            if min_change_change == 1:
                break
    return min_change_change
