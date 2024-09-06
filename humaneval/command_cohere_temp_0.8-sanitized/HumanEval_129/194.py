def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [i for i in range(N)]
    for i in range(1, k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0)]:
                if 0 <= nei[0] < N and nei[1] in (-1, 0, 1) and grid[j][nei[0]] < dp[i][j]:
                    dp[i][j] = grid[j][nei[0]]
                    start[j] = nei[0]
    result = [start[j] for j in range(N) if dp[k][j] == k]
    return result