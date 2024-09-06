def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for x in range(n):
                if i > 1 and grid[j][x] != grid[j][j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if i > 0 and grid[j][x] != grid[x][j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][x] + 1)
    ans = []
    j = k - 1
    while j >= 0:
        x = dp[k][j]
        ans.append(grid[j][x])
        j = x
    return ans[::-1]