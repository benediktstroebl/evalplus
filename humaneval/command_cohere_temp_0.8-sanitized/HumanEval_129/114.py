def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, 1)]:
                if 0 <= nei[0] < N and nei[1] == -1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][nei[0]] + grid[j][nei[0]])
                if 0 <= nei[0] < N and nei[1] == 1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][nei[0]] + grid[j][nei[0]])
    ans = []
    j = k - 1
    while j >= 0:
        ans.append(grid[j][0])
        j = dp[j][0]
    return ans[::-1]