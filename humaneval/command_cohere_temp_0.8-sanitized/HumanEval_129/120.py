def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0), (j, 2)]:
                if 0 <= nei[0] < n and 0 <= nei[1] < 2 and grid[nei[0]][nei[1]] < dp[i - 1][j]:
                    dp[i][j] = grid[nei[0]][nei[1]]
    return dp[k][0]