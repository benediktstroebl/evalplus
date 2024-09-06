def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1)]

    for i in range(k + 1):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, -1), (j - 1, 0), (j - 1, 1), (j, 1), (j + 1, 1), (j + 1, 0)]:
                if 0 <= nei[0] < N and 0 <= nei[1] < N:
                    if grid[nei[0]][nei[1]] < dp[i][j]:
                        start = nei
                        dp[i][j] = grid[nei[0]][nei[1]]

    res = []
    while k:
        nei = start
        while nei != (nei[0], nei[1]):
            res.append(dp[k][nei[0]])
            nei = (nei[0] + dp[k][nei[0]], nei[1] + dp[k][nei[0]])
        res.append(dp[k][nei[0]])
        k -= 1

    return res[::-1]