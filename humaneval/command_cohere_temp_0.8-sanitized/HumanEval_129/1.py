def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1)]

    for i in range(k + 1):
        for j in range(N):
            for nei in [(j + 1, 0), (j - 1, 0), (0, j + 1), (0, j - 1)]:
                if nei[0] < 0 or nei[1] < 0 or nei[0] >= N or nei[1] >= N:
                    continue
                if grid[nei[0]][nei[1]] < dp[i][j]:
                    dp[i][j] = grid[nei[0]][nei[1]]
                    start.append((nei[0], nei[1]))

    ans = []
    curr = start[0]
    for _ in range(k):
        ans.append(dp[k][curr[0]][curr[1]])
        curr = start[curr[0] + 1][curr[1]]

    return ans