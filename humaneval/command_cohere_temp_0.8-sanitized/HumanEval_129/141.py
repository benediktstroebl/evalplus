def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [-1, 0, 1]:
                if 0 <= nei < n and grid[j][nei] >= dp[i][nei] + 1:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][nei] + 1)
    return [grid[j][dp[k][j]] for j in range(n)]