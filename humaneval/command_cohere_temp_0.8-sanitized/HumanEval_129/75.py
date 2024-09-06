def minPath(grid, k):
    n = len(grid)
    if k > n * n or k <= 0:
        return []

    # Create a 2D list to store the paths up to length k
    dp = [[[0] * (n * n + 1) for _ in range(k + 1)] for _ in range(n + 1)]

    start = [(0, 0) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for l in range(1, k + 1):
                if grid[i - 1][j - 1] <= l:
                    dp[i][j][l] = dp[i - 1][j - 1][l - 1]
                else:
                    dp[i][j][l] = dp[i - 1][j - 1][l]
                    start[i] = (min(start[i - 1], start[i]), j)

    # Find the minimum path
    minPath = []
    i, j = start[n]
    for l in range(1, k + 1):
        if dp[n][j][l] != 0:
            minPath.append(dp[n][j][l])
            if l < k:
                j = (j + dp[n][j][l] - 1) % n

    # Reverse the min path to ensure lexicographic order
    minPath.reverse()
    return minPath