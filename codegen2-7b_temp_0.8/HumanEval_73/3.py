
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
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(1, n):
        for j in range(n):
            if arr[i-1] == arr[j]:
                arr[i] = arr[i-1]
            if arr[j-1] == arr[i]:
                arr[j] = arr[j-1]
    print(arr)
    return min(arr
