def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right)]:
                if nei[0] + 1 == nei[1] or nei[0] + 1 == j or nei[1] + 1 == j:
                    continue
                if dp[i][j] > dp[i][nei[0]] + 1:
                    dp[i + 1][nei[1]] = dp[i][nei[0]] + 1
    ans = []
    for i in range(1, k + 1):
        for j in range(n):
            if dp[i][j] == float('inf'):
                continue
            ans.append(grid[j][i - 1])
    return ans[::-1]