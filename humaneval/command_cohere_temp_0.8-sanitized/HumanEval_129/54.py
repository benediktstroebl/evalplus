def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for nei in [(j - 1, -1), (j, 0), (j + 1, 1)]:
                if 0 <= nei[0] < n and 0 <= nei[1] < 3 and grid[nei[0]][nei[1]] != grid[j][0]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][nei[0]] + 1)
    ans = [grid[j][0] for j in range(n) if dp[k][j] == k]
    return ans