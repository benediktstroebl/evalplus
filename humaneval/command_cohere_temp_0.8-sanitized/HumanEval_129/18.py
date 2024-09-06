def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    edges = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i > 0 and j > 0:
                edges[i][j] = min(edges[i - 1][j], edges[i][j - 1]) + 1
            if i > 0:
                edges[i][j] = min(edges[i - 1][j], edges[i][j])
            if j > 0:
                edges[i][j] = min(edges[i][j - 1], edges[i][j])

    for i in range(k + 1):
        for j in range(n):
            if i == 0:
                dp[i][j] = grid[j][0]
            else:
                dp[i][j] = float('inf')
                for nei in range(n):
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + edges[j][nei] + grid[nei][j - 1])
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + edges[j][nei] + grid[nei][j])
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + edges[i][nei] + grid[i][nei])

    ret = [0] * k
    j = n - 1
    i = k - 1
    while i >= 0 and j >= 0:
        if dp[i][j] != float('inf') and dp[i][j] == ret[-1]:
            ret.pop()
            if len(ret) == k:
                break
        ret.append(grid[j][i])
        j -= 1
        i -= 1

    return ret