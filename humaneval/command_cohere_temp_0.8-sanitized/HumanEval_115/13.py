import math
def max_fill(grid, capacity):
    """
    Use buckets to empty wells of water. Return number of times we need to lower the bucket.
    """
    # Create a 2D counter for each row/column to store water units.
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    # Count units of water for each well.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                dp[i][j] = dp[i][j-1] + dp[i-1][j] + 1
    
    # Calculate maximum water units that can be stored in a single bucket.
    max_capacity = math.ceil(math.sqrt(capacity))
    
    # Return maximum number of times we need to lower the bucket.
    return sum(max_capacity for row in dp for _ in row)