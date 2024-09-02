
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
    if not grid:
        return 0

    grid_len = max(grid.shape)
    nrows, ncols = grid_len, grid[0].shape[1]
    filled = [[0] * (ncols + 1) for j in range(nrows)]

    # mark all cells as not filled
    for i in range(nrows):
        for j in range(ncols):
            filled[i][j] = 1

    filled[0][0] = 1 # fill first well

    for k in range(1, grid_len):
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    if filled[i][j - 1] > 0:
                        filled[i][j] = filled[i][j - 1]
                        filled[i][j - 1] = 0
                    else:
                        filled[i][j] = 1

        for i in range(nrows):
            for j in range(ncols):
                if filled[i][j] > 0:
                    if filled[i][j - 1] > 0:
                        filled[i][j] = max(filled[i][j], filled[i][j - 1])
                    else:
                        filled[i][j] = 1

    return filled[0][0]

