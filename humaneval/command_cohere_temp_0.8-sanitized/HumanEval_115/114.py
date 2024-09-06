import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be collected from wells in a grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize a 2D DP array to store the maximum water that can be collected from each cell
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the bottom-right corner
    dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]
    
    # Fill the DP array using a bottom-up approach
    for i in range(rows - 2, -1, -1):
        for j in range(cols - 2, -1, -1):
            # If the current cell is a well, consider two possibilities:
            # 1. Extract water from the current cell and subtract capacity from the bucket.
            # 2. Skip the current cell and proceed with the next one, subtracting only capacity.
            dp[i][j] = max(grid[i][j], capacity + dp[i + 1][j] - capacity, dp[i][j + 1] - capacity)
    
    # The result is the maximum amount of water that can be collected
    return dp[0][0]
grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
capacity = 2