def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    for i in range(k + 1):
        dp[i][0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            minVal = min(dp[j - 1][i - 1], dp[j - 1][i])
            for x in range(i):
                dp[j][x + 1] = min(dp[j][x + 1], minVal + grid[i - 1][x])
    ans = []
    i = k
    while i > 0:
        ans.append(grid[n - 1][i - 1])
        i -= 1
    return ans[::-1]  # Return the list in reverse order to match the spec's ordering.