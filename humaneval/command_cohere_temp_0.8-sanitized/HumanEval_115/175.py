import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from a grid of wells.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a 2D DP array to store the maximum water that can be extracted from each cell.
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Initialize the DP array with the water capacity of each cell.
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                dp[i][j] = capacity
            else:
                dp[i][j] = 0
    
    # Iterate through the DP array upractices of grid[0][0]l applying the optimal substructure property.
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 1:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # Return the total number of units of water that can be extracted.
    return sum(dp[-1][:])
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
capacity = 1