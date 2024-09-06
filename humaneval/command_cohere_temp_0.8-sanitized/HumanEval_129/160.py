def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    for i in range(k + 1):
        dp[i][0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            dp[j][i] = min(dp[j][i - 1], dp[j - 1][i])
            if grid[i - 1][j - 1] < dp[j][i]:
                dp[j][i] = grid[i - 1][j - 1]
    return dp[k][-1]