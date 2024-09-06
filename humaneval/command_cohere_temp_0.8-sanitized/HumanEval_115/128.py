import math
def max_fill(grid, capacity):
    """
    Calculate the maximum water that can be fetched from wells.
    
    Args:
    - grid (List[List[int]]): rectangular grid of wells, each represented by a row of ones and zeros.
    - capacity (int): capacity of the bucket
    
    Returns:
    - int: Maximum number of times you need to lower the bucket to empty the wells.
    """
    # Calculate the maximum number of 1s in each row and column
    row_max = max(row[:] for row in grid)
    col_max = max(grid[i][:] for i in range(len(grid)))
    
    # Calculate the maximum total number of 1s that can be fetched
    # It can fetch max(row_max, col_max) * capacity at each location
    # So the total is sum(row_max, col_max) * capacity * 2
    return math.ceil(sum(min(row_max, col_max)) * capacity * 2)