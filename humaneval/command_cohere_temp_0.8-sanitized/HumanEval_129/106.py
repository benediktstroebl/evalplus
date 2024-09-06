def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k+1)]
    for i in range(k+1):
        dp[i][0] = 0
    for i in range(1, k+1):
        for j in range(N):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[j][i-1]
    return dp[k][-1]