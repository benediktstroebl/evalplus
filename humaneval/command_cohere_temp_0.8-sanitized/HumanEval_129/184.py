def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0), (j, 2)]:
                nei_row, nei_col = nei
                if nei_row == -1 and nei_col == -1:
                    continue
                if 0 <= nei_row < N and 0 <= nei_col < N:
                    dp[i + 1][nei_row] = min(dp[i + 1][nei_row], dp[i][j] + grid[j][nei_row])
                    dp[i][nei_col] = min(dp[i][nei_col], dp[i][j] + grid[j][nei_col])
    ans = [0] * k
    j = N - 1
    i = k - 1
    while i >= 0 and j >= 0:
        if dp[i][j] != float('inf'):
            break
        i -= 1
        j -= 1
    while i >= 0:
        ans[k - 1 - i] = grid[j][i]
        i -= 1
    while j >= 0:
        ans[k - 1 - j] = grid[j][N - 1 - j]
        j -= 1
    return ans