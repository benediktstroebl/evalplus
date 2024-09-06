
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
    number_of_fills = 0
    # number of wells
    n = len(grid)
    # number of units of water
    m = len(grid[0])
    # total water in the grid
    total_water = 0
    # find the total water
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                total_water += 1
    # total number of times the bucket needs to be lowered
    water_left = total_water
    # while there is water in the grid
    while water_left > 0:
        # initialize water_in_bucket
        water_in_bucket = capacity
        # find the maximum number of water we can extract from the grid
        for i in range(n):
            for j in range(m):
                # we can extract the lesser of the two
                water_left = min(water_left, grid[i][j])
                # we can extract the lesser of the two
                water_in_bucket = min(water_in
