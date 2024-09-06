def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nei = (j + dx, i + dy)
                    if 0 <= nei[0] < n and 0 <= nei[1] < k and grid[j][nei[0]] < dp[nei[1]][nei[0]]:
                        dp[nei[1]][nei[0]] = grid[j][nei[0]]
    ans = [dp[k][i] for i in range(n)]
    return sorted(ans)