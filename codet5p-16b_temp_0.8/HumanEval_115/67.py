
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

    def calculate_curr_well_capacity(well_row, well_col, well_grid, bucket_capacity):
        for i in range(well_col, len(well_grid[0])):
            if well_grid[well_row][i] == 1:
                return bucket_capacity
            bucket_capacity -= well_grid[well_row][i]
        return 0

    def calculate_next_well_capacity(well_row, well_col, well_grid, bucket_capacity):
        for i in range(well_col, -1, -1):
            if well_grid[well_row][i] == 1:
                return bucket_capacity
            bucket_capacity -= well_grid[well_row][i]
        return 0

    def calculate_next_well_capacity_helper(well_row, well_col, well_grid, bucket_capacity):
        if calculate_next_well_capacity(well_row, well_col, well_grid, bucket_capacity) > 0:
            return 1
        elif calculate_curr_well_capacity(well_
