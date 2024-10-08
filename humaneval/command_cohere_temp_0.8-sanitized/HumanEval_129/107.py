def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for x in range(n):
                if grid[j][x] > grid[j][x + 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][x] + 1)
                elif grid[j][x] > grid[j + 1][x]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][x] + 1)
                elif grid[j][x] > grid[x][j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, dp[i - 1][x] + 1)
    ans = []
    j = k - 1
    i = k - 1
    while i >= 0 and j >= 0:
        if dp[i][j] != float('inf'):
            break
        i -= 1
        j -= 1
    while i >= 0:
        ans.append(grid[j][i])
        i -= 1
        j -= 1
    ans.reverse()
    return ans