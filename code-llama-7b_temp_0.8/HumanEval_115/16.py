
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
    # 0 -> 0
    # 1 -> 1
    # -1 -> any
    def fill_water(grid, bucket_capacity):
        import numpy as np
        import math

        def find_water(grid):
            filled_count = 0
            for col in range(len(grid[0])):
                for row in range(len(grid)):
                    if grid[row][col] == 0:
                        filled_count += 1
            return filled_count

        def find_max_water_filled(grid, bucket_capacity):
            # find the highest filled
            max_filled = 0
            max_filled_row = 0
            max_filled_col = 0
            for col in range(len(grid[0])):
                for row in range(len(grid)):
                    if grid[row][col] != 0:
                        if max_filled < grid[row][col]:
                            max_filled = grid[row][col]
                            max_filled_row = row
                            max_filled_col = col
            return max_filled_row, max_filled_col

        # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        def fill_water_from_well(grid, bucket_capacity, well_row, well_col, total_filled):
            # return
            # 1 -> if filled the well
            # 0 -> if not filled
            # -1 -> if cant fill
            # cannot fill
            if bucket_capacity < 1:
                return -1
            # can fill
            if grid[well_row][well_col] == 0:
                return 0
            # filled
            if grid[well_row][well_col] == 1:
                return 1
            # if 0 -> 1
            grid[well_row][well_col] = 1
            total_filled += 1
            # left
            if well_col == 0:
                return total_filled
            else:
                return fill_water_from_well(grid, bucket
