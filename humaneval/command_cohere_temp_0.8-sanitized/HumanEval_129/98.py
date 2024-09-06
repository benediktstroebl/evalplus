def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for dx in range(4):
                nei = (j + dx) % n
                if 0 <= nei < n and grid[j][nei] < dp[i - 1][nei]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][nei] + 1)
    ans = []
    j = n - 1
    for i in range(k, 0, -1):
        while j >= 0 and dp[i][j] != i:
            j = (j - 1) % n
        if j < 0:
            return []  # No valid path
        ans.append(grid[j][0])
        j = (j + 1) % n
    return ans[::-1]  # Return reversed list to maintain lexicographical order