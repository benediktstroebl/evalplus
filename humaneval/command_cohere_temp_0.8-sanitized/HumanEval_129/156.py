def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right)]:
                if nei[0] == j:
                    continue
                nei_value = grid[nei[0]][nei[1]]
                if i + 1 < k and dp[i + 1][nei_value] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i + 1][nei_value] + 1)
                elif nei_value != n * n:
                    dp[i][j] = min(dp[i][j], dp[i][nei_value] + 1)
    ans = []
    for i in range(k):
        ans.append(dp[i][n - 1])
    return ans
left = lambda x: x - 1
right = lambda x: x + 1