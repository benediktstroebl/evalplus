def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Initialize the dp values to be the cell values of the first row
    dp = [row[0] for row in grid]
    for i in range(1, k + 1):
        new_dp = []
        for j in range(N):
            min_value = min(dp[j - 1], dp[j], grid[j][j - 1]) if j > 0 and j < N - 1 else dp[j]
            new_dp.append(min_value)
            dp = new_dp
    return dp[:k]