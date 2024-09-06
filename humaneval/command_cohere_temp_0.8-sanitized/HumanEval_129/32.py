def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nei = (j + dx) % n
                    if 0 <= nei < n and grid[j][nei] <= i:
                        dp[i][nei] = min(dp[i][nei], dp[i - 1][j] + 1)
    ans = []
    j = n - 1
    i = k - 1
    while i >= 0 and j >= 0:
        while j >= 0 and grid[j][n - 1] <= i:
            ans.append(grid[j][n - 1])
            j = (j - 1) % n
        while i >= 0 and dp[i][j] == k:
            ans.append(grid[j][i])
            i -= 1
        j -= 1
    return ans[::-1]