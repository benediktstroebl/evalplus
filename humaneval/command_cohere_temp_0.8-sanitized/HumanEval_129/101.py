def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(N):
            for nei in [-1, 0, 1]:
                if 0 <= nei < N and grid[j][nei] != grid[j][j]:
                    dp[i][nei] = min(dp[i][nei], dp[i - 1][j] + 1)
    ans = []
    j = N - 1
    for i in range(k, 0, -1):
        while j >= 0 and dp[i][j] == dp[i - 1][j] + 1:
            ans.append(grid[j][j])
            j = N - 1
            if len(ans) == k:
                return ans
    return ans