def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k):
        for j in range(N):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_val = grid[nei[0]][nei[1]]
                if nei_val < dp[i + 1][nei[0]]:
                    dp[i + 1][nei[0]] = nei_val
                    if i + 1 < k:
                        dp[i + 1][nei[0]] = min(dp[i + 1][nei[0]], dp[i + 1][nei[1]])
                    if i > 0 and nei_val < dp[i][nei[1]]:
                        dp[i][nei[1]] = nei_val
                    if i > 1 and nei_val < dp[i - 1][nei[1]]:
                        dp[i - 1][nei[1]] = nei_val
    ans = [grid[i][j] for i, j in zip(*[(row, col) for row, col, val in enumerate(dp[-1]) if val == dp[0][col]])]
    return ans