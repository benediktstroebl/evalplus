
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    else:
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        dp[0][n] = 1
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i % 2 == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][n]
