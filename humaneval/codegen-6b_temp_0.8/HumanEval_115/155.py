
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
    import math
    import numpy as np

    ROW = len(grid)
    COL = len(grid[0])
    next_wells = np.zeros((ROW, COL))

    for row in range(ROW):
        for col in range(COL):
            well = grid[row][col]
            if well == 1:
                bucket_num = math.floor(capacity / grid[row][col])
                next_wells[row][col] = bucket_num
                for r in range(row, -1, -1):
                    if grid[r][col] == 1:
                        next_wells[r][col] += bucket_num
                        grid[r][col] -= bucket_num
                        capacity -= bucket_num
                        if bucket_num > 1:
                            break
                        if grid[r][col] == 0 and high_pos_row(r, grid, next_wells) == -1:
                            next_wells[high_pos_row(r, grid, next_wells)][high_pos_col(r, grid, next_wells)] += bucket_num
                            grid[r][col] = 0
                            capacity -= bucket_num
                            break
                    if capacity == 0:
                        break

    return next_wells.sum()

