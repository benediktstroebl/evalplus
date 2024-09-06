def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1)]

    for i in range(k + 1):
        for j in range(N):
            for nei in [(j + 1, 0), (j - 1, 0), (0, j + 1), (0, j - 1)]:
                if nei[0] < 0 or nei[1] < 0 or nei[0] >= N or nei[1] >= N:
                    continue
                if grid[nei[0]][nei[1]] != i + 2:
                    continue
                cost = dp[i][j] + 1
                if cost < dp[i + 1][nei[0]]:
                    dp[i + 1][nei[0]] = cost
                    start.append(nei)

    ret = [grid[i][j] for i, j in start]
    return ret