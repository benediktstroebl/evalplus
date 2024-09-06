def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j, 0), (j + 1, 1)]:
                nx, ny = nei
                if 0 <= nx < N and 0 <= ny < k and grid[nx][ny] < dp[i][j]:
                    dp[i][j] = grid[nx][ny]
    return dp[k][0]