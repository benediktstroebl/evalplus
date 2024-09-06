def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0), (j, 2)]:
                nei_row, nei_col = nei
                if nei_row < 0 or nei_col < 0 or nei_row >= N or nei_col >= N:
                    continue
                if grid[nei_row][nei_col] != j + 1:
                    continue
                for ni in range(i + 1, k + 1):
                    dp[ni][nei_row] = min(dp[ni][nei_row], dp[i][j] + 1)
    ans = []
    for i in range(k, 0, -1):
        ans.append(grid[dp[i][0]][0])
    return ans[::-1]