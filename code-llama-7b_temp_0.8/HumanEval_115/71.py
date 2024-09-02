
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
    def max_water_helper(grid, bucket_capacity):
        # Depth first search, mark the max water level by height
        max_water_level = 0
        max_water_level_bucket = None
        max_water_level_position = None
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                # Skip already filled cells
                if grid[row_index][col_index] == 0:
                    continue
                # Skip already filled cells
                if grid[row_index][col_index] == 1:
                    grid[row_index][col_index] = 0
                    continue
                # Skip already filled cells
                if max_water_level_bucket != None and max_water_level_position != None:
                    continue
                # Get max water level
                max_water_level, max_water_level_bucket, max_water_level_position = max_water_level_helper(grid, bucket_capacity, row_index, col_index, 0)
        return max_water_level
    
    def max_water_level_helper(grid, bucket_capacity, row_index, col_index, water_level):
        # Depth first search, mark the max water level by height
        water_level_update = 0
        max_water_level = 0
        max_water_level_bucket = None
        max_water_level_position = None
        # check the water level is valid
        if row_index >= len(grid) or col_index >= len(grid[0]):
            return max_water_level, max_water_level_bucket, max_water_level_position
        # check the water level is valid
        if grid[row_index][col_index] != 0:
            return max_water_level, max_water_level_bucket, max_water_level_position
        # check the water level is valid
        if water_level > max_water_level:
            max_water_level = water_level
        # check the water level is valid
        if water_level > bucket_cap
