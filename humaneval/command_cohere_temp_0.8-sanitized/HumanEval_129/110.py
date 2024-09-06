def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0), (j, 2)]:
                if 0 <= nei[0] < N and 0 <= nei[1] < 2 and grid[nei[0]][nei[1]] < dp[i][j]:
                    dp[i + 1][nei[0]] = grid[nei[0]][nei[1]]
                    for x in range(j):
                        dp[i + 1][x] = min(dp[i + 1][x], dp[i][j])
    return dp[k][0]