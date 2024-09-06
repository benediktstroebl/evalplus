def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []
    dp = [float('inf')] * N
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0:
                dp[i] = min(dp[i], grid[i][j])
            elif grid[i][j] < dp[i-1] or (grid[i][j] == dp[i-1] and grid[i][j] < dp[i-1]-1):
                dp[i] = grid[i][j]
    result = []
    for i in range(k):
        result.append(dp[0]//N)
        dp[0] -= N*result[-1]
    return result[::-1]