def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k+1)]
    start = [i for i in range(N) if grid[i][0] == 1]
    if not start:
        return []

    for i in range(k, 0, -1):
        for j in range(N):
            for n in range(N):
                if i == k or (grid[j][n] != grid[j][n-1] and dp[i-1][n-1] > dp[i-1][j] + 1):
                    dp[i][j] = dp[i-1][n-1] if i > 0 else 1
                    if grid[j][n] != grid[j][n-1]:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)

    ans = [0] * k
    j = start[0]
    for i in range(k):
        while j == start[0] and grid[j][0] == i + 1:
            j = (j + 1) % N
        ans[i] = grid[j][0]
        j = (j + 1) % N
    return ans[::-1]