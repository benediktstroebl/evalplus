
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
    import numpy as np
    import math
    
    # The number of water units
    n_water_units = np.sum(grid)
    # The number of rows and columns in the grid
    n_rows, n_cols = grid.shape
    # The number of wells
    n_wells = n_rows*n_cols
    # The number of buckets
    n_buckets = n_wells - n_water_units
    # The capacity of each bucket
    bucket_capacity = capacity
    
    # The number of buckets needed to empty all the wells
    n_buckets_needed = math.ceil(n_water_units/bucket_capacity)
    
    return n_buckets_needed
