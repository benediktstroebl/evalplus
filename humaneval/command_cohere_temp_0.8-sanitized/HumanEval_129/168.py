def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for x in range(n):
                dp[i][j] = min(dp[i][j], dp[i - 1][x] + grid[x][j])
    ans = []
    i, j = k - 1, n - 1
    while i >= 0 and j >= 0:
        ans.append(grid[i][j])
        i, j = i - 1, j - k
    ans.reverse()
    return ans