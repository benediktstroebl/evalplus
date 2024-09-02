
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
    arr1 = [i for i in arr]
    for i in range(n//2, -1, -1):
        arr1.append(arr1.pop(0))
    for i in range(n):
        if arr1[i] != arr1[n-i-1]:
            return n
    return n-1