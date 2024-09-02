
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

    def max_well(grid, capacity, x, y):
        import math
        import pdb
        """
        Find the maximum number of wells that can be filled from a given point
        """
        nrows = len(grid)
        ncols = len(grid[0])
        # pdb.set_trace()
        # print(grid)
        well_count = 0
        for row in range(x, nrows):
            for col in range(y, ncols):
                if grid[row][col] > 0:
                    well_count += 1
        for row in range(x, nrows):
            for col in range(y, ncols):
                if grid[row][col] > 0:
                    grid[row][col] = 0
                    well_count += max_well(grid, capacity, row + 1, col)
        return well_count

    nrows = len(grid)
    ncols = len(grid[0])
    well_count = 0
    for row in range(nrows):
        for col in range(ncols):
            if grid[row][col] > 0:
                well_count += max_well(grid, capacity, row, col)
    return well_count
