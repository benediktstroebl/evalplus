def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    for i in range(n):
        for j in range(n):
            dp[0][i] = grid[i][j]
    for length in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if dp[length - 1][i] == float('inf'):
                    continue
                for nei in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= nei[0] < n and 0 <= nei[1] < n:
                        dp[length][nei[0]] = min(dp[length][nei[0]], dp[length - 1][i] + grid[nei[0]][nei[1]])
    ans = []
    for i in range(k, -1, -1):
        ans.extend(dp[i][n - 1])
    return ans[::-1]