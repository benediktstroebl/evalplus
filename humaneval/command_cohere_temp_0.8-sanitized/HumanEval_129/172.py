def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right)]:
                if nei[0] < 0 or nei[0] >= n or nei[1] < 0:
                    continue
                if dp[i][j] > dp[i - 1][nei[0]] + 1:
                    dp[i][j] = dp[i - 1][nei[0]] + 1
                    if i < k:
                        dp[i][j] = min(dp[i][j], dp[i][nei[0]])
    ans = [grid[j][i - 1] for i in range(k)]
    return ans
def left(j):
    return max(j - 1, 0)
def right(j):
    return min(j + 1, 9)