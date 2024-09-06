def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right)]:
                if nei[0] == j:
                    continue
                nei_cell = (nei[0], nei[1])
                if nei_cell not in [(j, left), (j, right)]:
                    continue
                nei_value = grid[nei[0]][nei[1]]
                if i + 1 < k and (dp[i + 1][nei_cell[0]] == float('inf') or dp[i + 1][nei_cell[0]] > nei_value):
                    dp[i + 1][nei_cell[0]] = nei_value
                if i > 0 and dp[i][j] > dp[i - 1][j] + 1 and dp[i - 1][j] + 1 < nei_value:
                    dp[i][j] = dp[i - 1][j] + 1
    ans = [grid[j][i] for i in range(n) for j in range(n) if dp[k][j] == dp[k][j] + 1 and grid[j][i] == dp[k][j]]
    return ans