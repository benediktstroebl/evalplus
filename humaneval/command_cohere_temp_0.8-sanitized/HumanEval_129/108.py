def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1)]

    for i in range(k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, -1), (j - 1, 0), (j, 0), (j + 1, 0), (j - 1, 1), (j, 1), (j + 1, 1)]:
                if nei[0] < 0 or nei[0] >= N or nei[1] < 0 or nei[1] >= N:
                    continue
                if grid[nei[0]][nei[1]] < dp[i][j]:
                    dp[i][j] = grid[nei[0]][nei[1]]
                    start[i] = nei

    res = [start[k][0] * N + start[k][1] for k in range(k + 1)]
    res.reverse()
    return res