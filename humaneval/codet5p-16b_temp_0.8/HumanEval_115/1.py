
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

    def empty_well(grid, capacity):
        bucket_count = 0
        total_capacity = 0
        for row in grid:
            for bucket in row:
                total_capacity += bucket
        return total_capacity
    
    if not grid or not capacity:
        return 0
    empty_bucket = empty_well(grid, capacity)
    if empty_bucket == capacity:
        return 0
    
    grid = grid.copy()
    
    def get_well_val(i, j):
        return grid[i][j]
    
    def set_well_val(i, j, val):
        if val == 1:
            grid[i][j] = 1
        elif val == 0:
            grid[i][j] = 0
        else:
            raise ValueError("value must be 0 or 1")
    
    def get_well_capacity(i, j):
        return capacity
    
    def set_well_capacity(i, j, val):
        pass
    
    def is_within_bounds(i, j):
        
