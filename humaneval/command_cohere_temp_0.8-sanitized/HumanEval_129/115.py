def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for di in (-1, 0, 1):
                nei = (j + di) % n
                if nei < 0 or nei == j or grid[j][nei] != j + 1:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - 1][nei] + 1)
    ans = []
    j = n - 1
    i = k - 1
    while i >= 0 and j >= 0:
        while j >= 0 and dp[i][j] != float('inf'):
            ans.append(j + 1)
            j = (j - 1) % n
        i -= 1
        j = (j - 1) % n
    return ans[::-1]