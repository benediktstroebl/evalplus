def minPath(grid, k):
    # Calculate number of rows and columns
    N = len(grid)
    M = len(grid[0])

    # 2D DP to track if a path of length 'i' can start from cell [r, c]
    dp = [[False] * M for _ in range(N)]
    
    # Initialize the first column as a valid starting point for path of any length
    for r in range(N):
        dp[r][0] = True

    # Solve using 2D DP
    paths = [[None] * M for _ in range(k + 1)]
    for r in range(N):
        for c in range(M):
            if dp[r][c] and grid[r][c] not in paths[k]:
                paths[k].append(grid[r][c])
                for i in range(1, k + 1):
                    prev_col = (c - i + M) % M
                    next_col = (c + 1) % M
                    dp[r][next_col] |= dp[r][prev_col]
                    if dp[r][next_col]:
                        paths[i].append(grid[r][next_col])
    
    return paths[k]