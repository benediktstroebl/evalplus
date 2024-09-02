
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
    if not grid or not grid[0]:
        return 0
    row_num = len(grid)
    col_num = len(grid[0])
    max_well_num = row_num * col_num
    # init
    well_num = 0
    well_filling_num = 0
    # search
    for i in range(row_num):
        well_filling_num += (grid[i].count(1)) * capacity 
        well_num += (grid[i].count(1))
        if well_filling_num > max_well_num:
            well_filling_num -= well_num * capacity
            well_num -= grid[i].count(1)
            return well_filling_num // capacity
    return 0
