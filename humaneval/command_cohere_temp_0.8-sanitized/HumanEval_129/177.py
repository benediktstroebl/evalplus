def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for x in range(n):
                if grid[j][x] != grid[j][j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][x] + 1)
    ans = []
    for i in range(k, -1, -1):
        for j in range(n - 1, -1, -1):
            if grid[j][n - 1] != grid[j][j]:
                if dp[i][j] == dp[i][n - 1] + 1:
                    ans.append(grid[j][n - 1])
                    j = n - 1
    reverse(ans)
    return ans