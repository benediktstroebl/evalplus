def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for x in range(n):
                if grid[j][x] < grid[j][x - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][x - 1] + 1)
    ans = []
    j = k - 1
    while j >= 0:
        x = dp[j][n - 1]
        while x >= 0:
            ans.append(grid[j][x])
            x = dp[x][x - 1]
        j -= 1
    return ans[::-1]