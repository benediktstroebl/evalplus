def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(N):
            for di in range(N):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[di][j])
    ans = []
    i, j = k - 1, N - 1
    while i >= 0 and j >= 0:
        ans.append(grid[i][j])
        i = i - 1
        j = j - 1
    ans.reverse()
    return ans