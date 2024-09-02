
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

    # ------------------------------------------------------------------
    # Solution:
    #   1. If the number of wells is less than the capacity, then the max 
    #   number of iterations to fill all buckets is the minimum number of wells.
    #   2. If the number of wells is greater than the capacity, then the max
    #   number of iterations to fill all buckets is the minimum number of wells
    #   divided by the capacity.
    # ------------------------------------------------------------------
    
    def count_water_in_wells(grid):
        wells = 0
        for row in grid:
            for cell in row:
                if cell == 1:
                    wells += 1
        return wells

    wells = count_water_in_wells(grid)
    if wells < capacity:
        return wells
    else:
        return math.ceil(wells / capacity)
    
