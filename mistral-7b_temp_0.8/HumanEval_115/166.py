
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

    # My solution
    grid_len = len(grid)
    cols_len = len(grid[0])
    min_cols = min(grid_len, cols_len)
    water_count = 0
    water_col_count = 0
    bucket_capacity = capacity
    for i in range(min_cols):
        for j in range(min_cols):
            if grid[i][j] == 1:
                water_count += 1

        if water_count % bucket_capacity == 0:
            water_col_count += 1
        else:
            water_col_count += math.ceil(water_count / bucket_capacity)

        water_count = 0

    return water_col_count


