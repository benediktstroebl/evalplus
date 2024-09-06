def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right)]:
                if nei[1] == j:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - 1][nei[0]] + grid[j][nei[1]])
    res = [0] * k
    j = n - 1
    i = k - 1
    while i >= 0 and j >= 0:
        if dp[i][j] != float('inf'):
            res[k - 1 - i] = grid[j][n - 1 - j]
            j = neigbs[j]
        else:
            i -= 1
    return res[::-1]