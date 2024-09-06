def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [i for i in range(N)]
    for i in range(1, k + 1):
        for j in range(N):
            for n in range(N):
                if grid[j][n] != grid[j][j]:
                    start.remove(j)
                    break
            if not start:
                break
            cost = start.index(j) + 1
            for n in range(N):
                if grid[j][n] != grid[n][j]:
                    dp[i][n] = min(dp[i][n], dp[i - 1][n] + cost)
                    if not start:
                        break
                    start.remove(n)
    ans = [grid[i][j] for i, j in zip(start, start)]
    return ans