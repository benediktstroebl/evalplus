def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for di in (-1, 0, 1):
                nei = j + di
                if nei < 0 or nei >= n:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - 1][nei] + grid[j][nei])
    res = []
    j = k - 1
    while j >= 0:
        res.append(grid[0][j])
        j = (j - 1) // 3
    return res[::-1]