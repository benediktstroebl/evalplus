
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
    # create a grid for the water
    water_grid = [ [0] * len(grid[0]) for i in range(len(grid))]
    # fill the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                water_grid[i][j] = capacity

    # iterate through the grid and add water
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # fill the buckets
            bucket_grid = []
            # create a grid for the buckets
            for k in range(capacity):
                bucket_grid.append([0] * len(grid[0]))

            # add water to the buckets
            while True:
                # fill the buckets
                for k in range(capacity):
                    if water_grid[i][j] > 0:
                        bucket_grid[k][j] = min(bucket_grid[k][j
