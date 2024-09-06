
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
    
    def get_filled_wells(grid):
        filled_wells = 0
        for row in grid:
            if row.count(1) == len(row):
                filled_wells += 1
        return filled_wells
    
    def fill_well(grid, grid_size):
        if grid.count(1) == grid_size:
            return
        
        well_index = 0
        while grid[well_index][grid_size] == 1:
            well_index += 1
        grid[well_index][grid_size] = 1
        fill_well(grid, grid_size - 1)
        fill_well(grid, grid_size + 1)
        
    return get_filled_wells(grid)
    
