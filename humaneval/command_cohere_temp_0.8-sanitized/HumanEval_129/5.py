def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(N):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_val = grid[nei[0]][nei[1]]
                if nei_val < dp[i][j]:
                    dp[i + 1][nei[0]] = nei_val
                    for x in range(N):
                        if x != nei[0]:
                            dp[i + 1][x] = min(dp[i + 1][x], dp[i][j] + (nei_val - grid[nei[0]][nei[1]]))
    return [dp[k][i] for i in range(N)]