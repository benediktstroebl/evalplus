def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(N):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_ij = nei[0] + nei[1]
                if nei_ij < N and grid[nei_ij][nei[1]] != grid[j][nei[0]]:
                    dp[i + 1][nei_ij] = min(dp[i + 1][nei_ij], dp[i][j] + 1)
    ans = [grid[i][j] for i, j in reversed(dp[k]) if j == 0]
    return ans