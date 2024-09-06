def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_val = grid[nei[0]][nei[1]]
                if nei_val != grid[j][0] and dp[i][j] > dp[i][j] + 1:
                    dp[i + 1][nei[0]] = dp[i][j] + 1
    res = [grid[i][j] for i, j in reversed(dp[k][0]) if j == 0]
    return res