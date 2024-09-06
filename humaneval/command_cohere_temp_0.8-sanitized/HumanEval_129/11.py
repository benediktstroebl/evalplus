def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_ij = nei[0] + nei[1]
                if nei_ij < n and grid[nei_ij][nei[1]] < dp[i][nei[0]]:
                    dp[i + 1][nei_ij] = dp[i][nei[0]] + 1
    ans = [0] * k
    i, j = k - 1, 0
    while i >= 0 and j < n - 1:
        while j < n - 1 and grid[j][next_j] < dp[i][j]:
            j, next_j = next_j, (next_j + 1) % n
        ans[i] = grid[j][next_j]
        i, j = i - 1, next_j
    return ans[::-1]