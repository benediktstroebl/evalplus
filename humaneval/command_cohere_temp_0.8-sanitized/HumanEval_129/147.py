def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    for i in range(N):
        for j in range(N):
            dp[0][i] = grid[i][j]
    for length in range(1, k + 1):
        for start in range(N):
            for direction in range(4):
                x, y = start, direction
                if 0 <= x < N and 0 <= y < N:
                    dp[length][x] = min(dp[length][x], dp[length - 1][y] + grid[x][y])
    result = [dp[k][start] for start in range(N)]
    return result