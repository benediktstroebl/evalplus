
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i
        for j in range(1, n+1):
            if j == 0 or arr[j-1] <= arr[j]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1] + 1)
    return dp[n][n]