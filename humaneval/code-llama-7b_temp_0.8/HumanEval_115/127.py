
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
    #print(grid)
    import math

    # Find the maximum value in the grid.
    max_val = 0
    for row in grid:
        for val in row:
            if val > max_val:
                max_val = val

    #print(max_val)

    # How many times to we have to lower the bucket?
    # This will be equal to the number of total wells - bucket capacity + 1.
    # Then divide it by the bucket capacity.
    n_times = 0
    for row in grid:
        for val in row:
            if val > 0:
                n_times += val

    return int(math.ceil(n_times/(max_val*capacity)))
