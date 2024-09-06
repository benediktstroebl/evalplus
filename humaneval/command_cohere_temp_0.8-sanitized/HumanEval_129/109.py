def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    for i in range(N):
        for j in range(N):
            dp[0][i] = grid[i][j]
    for length in range(1, k + 1):
        for i in range(N):
            for j in range(N):
                if dp[length - 1][i] == float('inf'):
                    continue
                for di in range(N):
                    for dj in range(N):
                        if 0 <= i + di and 0 <= j + dj and grid[i + di][j + dj] != float('inf'):
                            dp[length][i] = min(dp[length][i], dp[length - 1][i] + (grid[i + di][j + dj] for _ in range(length - 1)))
    return dp[k][0]