
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
    min_change = float('inf')
    min_index = 0
    for i in range(n):
        for j in range(i, n, 1):
            if (arr[i] != arr[j]) and (arr[j] != arr[i] + n // 2):
                n -= 1
                arr[i], arr[j] = arr[j], arr[i] + n // 2
                min_change = min(min_change, n)
                min_index = j
    return min_change, min_index
