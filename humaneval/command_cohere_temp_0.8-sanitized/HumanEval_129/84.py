def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1) for _ in range(k + 1)]
    result = []
    
    # Initialize the first column as the shortest path
    for i in range(N):
        dp[0][i] = grid[0][i]
    
    for length in range(1, k + 1):
        for i in range(N):
            for j in range(N):
                # Ignore moving off the grid or repeating a cell
                if length == 1 or grid[i][j] != dp[length - 1][i]:
                    dp[length][j] = min(dp[length][j], dp[length - 1][i] + (1 if grid[i][j] < grid[i][j - 1] else 0))
                    
                    if dp[length][j] != float('inf'):
                        start[length] = (i, j)
                        
    path = []
    current = start[k]
    for i in range(k):
        path.append(grid[current[0]][current[1]])
        current = (current[0] + (1 if grid[current[0]][current[1]] < grid[current[0] - 1][current[1]] else 0), current[1])
    path.reverse()
    return path