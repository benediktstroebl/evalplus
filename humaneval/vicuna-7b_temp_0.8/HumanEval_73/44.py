
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
    if n == 1:
        return 0
    dp = [[0] * (n+1) for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + dp[i-1][n-i-1]
    for i in range(2, n):
        for j in range(i-1, n-i):
            dp[i][j] = dp[i-1][j] + dp[i][j+1]
    for j in range(2, n):
        for i in range(n-j-1):
            dp[j][i] = dp[j-1][i] + dp[j][i+1]
    return dp[n-1][0]
