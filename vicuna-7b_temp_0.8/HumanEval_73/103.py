
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
    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(1, n + 1):
        dp[0][i] = i
    for i in range(1, n):
        for j in range(1, n):
            for k in range(i, n):
                dp[i][j] = min(dp[i][j], dp[i-1][k-1] + dp[j][k])
    return dp[-1][-1]