def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [i for i in range(N)]
    dp[0][start[0]] = 0
    for i in range(1, k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0)]:
                nei_val = grid[nei[0]][nei[1]]
                if nei_val != N * N and dp[i - 1][nei_val] + 1 < dp[i][j]:
                    dp[i][j] = dp[i - 1][nei_val] + 1
                    start[j] = nei_val
    res = [start[0]]
    for i in range(1, k):
        res.append(start[res[i - 1]])
    return res