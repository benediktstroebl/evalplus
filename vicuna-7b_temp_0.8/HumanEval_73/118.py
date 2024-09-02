
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
    dp = [[0] * (len(arr) + 1) for _ in arr]
    dp[0][0] = arr[0]
    dp[-1][-1] = arr[-1]
    for i in range(1, len(arr)):
        if arr[i] != dp[i-1][0]:
            dp[i][0] = arr[i]
        else:
            dp[i][i-1] = arr[i]
    return dp[-1][-1] + 1