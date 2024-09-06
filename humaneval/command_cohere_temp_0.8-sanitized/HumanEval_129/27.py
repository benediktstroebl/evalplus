def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(N):
            for n in range(N):
                if abs(j - n) > i:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[n][j])
    ans = []
    j = N - 1
    for i in range(k, 0, -1):
        while j >= 0 and dp[i][j] != dp[i - 1][j]:
            j -= 1
        ans.append(grid[0][j])
        j -= 1
    return ans[::-1]