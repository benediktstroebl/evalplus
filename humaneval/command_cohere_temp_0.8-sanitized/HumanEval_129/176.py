def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1) for _ in range(k + 1)]
    result = []
    
    # Initialize the first column as the smallest value
    for i in range(N):
        dp[0][i] = grid[i][0]
        start[0] = (0, i)
    
    for length in range(1, k + 1):
        for i in range(N):
            for j in range(N):
                # Calculate the minimum value among the current cell and its neighbors
                min_val = min(dp[length - 1][(i - 1) % N] if (i - 1) >= 0 else float('inf'),
                             dp[length - 1][(i + 1) % N] if (i + 1) < N else float('inf'),
                             dp[length - 1][(j - 1) % N] if (j - 1) >= 0 else float('inf'),
                             dp[length - 1][(j + 1) % N] if (j + 1) < N else float('inf'))
                
                # Update the current cell if the minimum value is smaller
                if grid[i][j] < min_val:
                    dp[length][i] = min_val
                    start[length] = (i, j)
    
    # Trace back to find the minimum path
    i, j = start[k]
    while i >= 0 and j >= 0:
        result.append(grid[i][j])
        i = (i - 1) % N
        j = (j - 1) % N
    result.reverse()
    return result