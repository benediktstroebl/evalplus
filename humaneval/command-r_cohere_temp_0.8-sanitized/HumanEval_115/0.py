import math
def max_fill(grid, capacity):
    """
    Solves the bucket lowering problem.
    
    Args:
        grid (list): A list of lists representing the wells, where 1 denotes a unit of water.
        capacity (int): The capacity of the buckets.
        
    Returns:
        int: Number of times the bucket needs to be lowered.
    """
    rows = len(grid)
    cols = len(grid[0])
    steps = 0
    
    for r in range(rows):
        col = 0
        while col < cols:
            if grid[r][col] == 1:
                # Find the next column with water, if any
                next_col = col + 1
                while next_col < cols and grid[r][next_col] == 0:
                    next_col += 1
                
                num_buckets = math.ceil((grid[r][col] + grid[r][next_col - 1]) / capacity)
                steps += num_buckets
                col = next_col
            else:
                col += 1
    
    return steps