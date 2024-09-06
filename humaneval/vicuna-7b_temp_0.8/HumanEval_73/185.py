
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
    min_change = len(arr)
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            min_change_temp = min_change
            for k in range(i, j):
                min_change_temp -= arr[k] != arr[j-k]
                arr[k] = arr[j-k]
            arr[j] = arr[i]
            min_change = min_change_temp
    return min_change