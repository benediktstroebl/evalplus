def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    for i in range(N):
        for j in range(N):
            dp[0][i] = grid[i][j]
    for length in range(1, k + 1):
        for i in range(N):
            for j in range(N):
                dp[length][i] = min(dp[length][i], dp[length - 1][i])
                for nei in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= nei[0] < N and 0 <= nei[1] < N:
                        dp[length][i] = min(dp[length][i], dp[length - 1][nei[0]] + grid[nei[0]][nei[1]])
    return dp[k][0]