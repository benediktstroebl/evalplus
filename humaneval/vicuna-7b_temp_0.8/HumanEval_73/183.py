
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
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(i):
            if j == 0 or (j == i and arr[j] != arr[i-1]):
                dp[i][j] = dp[i-1][j-1]
    return dp[-1][n-1]
