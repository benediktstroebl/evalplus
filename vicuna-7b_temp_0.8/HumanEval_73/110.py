
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
    n = len(arr)
    min_change = n//2
    if n % 2 == 0:
        min_change = min_change-1
    array_ref = arr[0]
    for i in range(n-1):
        for j in range(i+1, n-1):
            if (arr[j] != array_ref):
                return min_change
        array_ref = arr[i+1]
    return min_change

