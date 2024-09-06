def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1)]

    for i in range(k + 1):
        for j in range(N):
            for nei in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + nei[0], j + nei[1]
                if ni < 0 or nj < 0 or ni >= k or nj >= N:
                    continue
                if grid[nj][ni] < dp[i][j]:
                    dp[i][j] = grid[nj][ni]
                    start[i] = (nj, ni)

    res = [start[k][1] for k in range(k)]
    res.reverse()
    return res