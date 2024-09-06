def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_ij = nei[0] + nei[1]
                if nei_ij < n and grid[nei_ij][nei[1]] < dp[i][j]:
                    dp[i + 1][nei_ij] = dp[i][j] + 1
    ans = []
    i, j = k, n - 1
    while i > 0 and j > 0:
        while j >= 0 and dp[i][j] == dp[i][j + 1]:
            j -= 1
        ans.append(grid[j][i - 1])
        i -= 1
        j = n - 1
    return ans[::-1]
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
k = 3