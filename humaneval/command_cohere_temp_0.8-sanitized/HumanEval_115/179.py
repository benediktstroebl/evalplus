import math
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Parameters:
        grid (list of list): Each list represents a well.
        capacity (int): Bucket capacity

    Returns:
        int: Number of times buckets need to be lowered
    """
    rows = len(grid)
    cols = len(grid[0])
    max_fill = 0
    for i in range(rows):
        current_fill = 0
        for j in range(cols):
            if grid[i][j] == 1:
                current_fill += 1
            else:
                max_fill = max(max_fill, current_fill)
                current_fill = 0
        max_fill = max(max_fill, current_fill)
    return max_fill - (rows * cols) // capacity