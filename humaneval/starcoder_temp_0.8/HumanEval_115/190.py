
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    if capacity == 0:
        return 0
    n_rows = len(grid)
    n_cols = len(grid[0])
    total_water = sum([sum(row) for row in grid])
    max_rows = math.floor(total_water/capacity)

    # Max rows don't fit in bucket capacity
    if max_rows == 0:
        return 0

    # Calculate number of times buckets can be lowered
    fills = 0
    rows_left = n_rows
    cols_left = n_cols
    while rows_left > max_rows:
        fills += cols_left
        rows_left -= max_rows
        cols_left = n_cols
    fills += (cols_left - (rows_left * n_cols))
    return fills

