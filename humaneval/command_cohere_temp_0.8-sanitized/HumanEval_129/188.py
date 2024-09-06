def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(N):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_val = grid[nei[0]][nei[1]]
                if nei_val < dp[i][j]:
                    dp[i + 1][nei[0]] = nei_val
                    for nx in range(N):
                        if nx != nei[0]:
                            dp[i + 1][nx] = min(dp[i + 1][nx], dp[i][j] + 1)
    ans = [dp[k][0]]
    for i in range(1, N):
        if dp[k][i] == dp[k][i - 1]:
            continue
        ans.append(grid[i][0])
    return ans