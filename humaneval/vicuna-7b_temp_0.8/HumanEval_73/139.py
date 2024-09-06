
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
    min_change = n
    min_change_idx = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] != arr[j]:
                break
        else:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                min_change -= 1
                min_change_idx = i
    return min_change