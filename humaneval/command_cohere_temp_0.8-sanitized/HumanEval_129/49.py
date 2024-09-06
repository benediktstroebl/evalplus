def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [-1, 0, 1]:
                if nei == 0:
                    continue
                ni = i + nei
                if ni >= k:
                    break
                dp[ni + 1][j] = min(dp[ni + 1][j], dp[i][j] + grid[j][nei])
    res = [grid[j][nei] for j in range(n) for nei in [-1, 0, 1] if dp[k][j] == dp[k][j] - grid[j][nei]]
    return res