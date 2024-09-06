def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_ij = nei[0] + nei[1]
                if nei_ij < n and grid[nei_ij][nei[1]] < dp[i][j]:
                    dp[i + 1][nei_ij] = dp[i][j]
                    dp[i + 1][nei_ij] = min(dp[i + 1][nei_ij], dp[i][nei_ij] + 1)
                    if i == k:
                        return [grid[j][l] for l in range(n) if dp[k][l] == dp[k][j]]
    return []
def left():
    return 0
def right():
    return 1