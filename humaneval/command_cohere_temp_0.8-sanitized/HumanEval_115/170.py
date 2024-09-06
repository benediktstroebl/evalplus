import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from wells using a fixed capacity bucket.
    
    Args:
        grid (list of list): Each sublist represents a well and contains 0s and 1s.
        capacity (int): The capacity of the bucket in terms of number of water units it can carry.

    Returns:
        int: The maximum number of times the bucket needs to be lowered to empty all wells.
    """
    rows, cols = len(grid), max(len(row) for row in grid)
    
    # Create a 2D DP array to store the maximum water extraction possibilities
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the DP values for boundaries
    dp[0][:] = grid[0]
    dp[-1][:] = grid[-1]
    
    for i in range(1, rows):
        for j in range(1, cols):
            # If both the current cell and its right neighbour have water, the maximum is their sum
            if grid[i][j] == 1 and dp[i-1][j-1] == 1:
                dp[i][j] = 1
            # If only the current cell has water, the maximum is the current cell itself
            elif grid[i][j] == 1:
                dp[i][j] = 1
            # If neither cell has water, the maximum is the maximum of the left cell and the current cell's capacity
            else:
                dp[i][j] = max(dp[i-1][j], capacity)
    
    return sum(row for row in dp if row == 1)
capacity = 1