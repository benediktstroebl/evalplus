
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
    min_diff = float('inf')
    for i in range(1, n):
        for j in range(i):
            if arr[j] != arr[i-1] and (arr[j-1] != arr[i-1] or arr[j-1] != arr[i-2]):
                return i
            elif arr[j] != arr[i-1] and arr[j-1] == arr[i-1]:
                return i
            elif arr[j] != arr[i-1] and arr[j-1] != arr[i-1] and arr[j] != arr[i-2]:
                return i
    return min_diff