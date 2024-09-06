def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_j, nei_i = nei
                if nei_i < 0 or nei_j < 0 or nei_i >= n or nei_j >= n:
                    continue
                if grid[nei_j][nei_i] != grid[j][i]:
                    continue
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][nei_j] + 1)
    ans = []
    for i in range(k, 0, -1):
        ans.extend(list(map(grid[j][:, i].index, range(dp[i][n - 1] + 1))))
    return ans