def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    starts = set(range(n * n))
    for i in range(k + 1):
        for j in range(n):
            for ny in range(n):
                if (i, j, ny) not in starts:
                    continue
                starts.remove((i, j, ny))
                dp[i][j] = grid[j][ny]
                for nz in range(n):
                    if (i, j, nz) not in starts:
                        continue
                    starts.remove((i, j, nz))
                    dp[i][j] = min(dp[i][j], grid[j][ny] + dp[i - 1][nz])
    return dp[k][0]