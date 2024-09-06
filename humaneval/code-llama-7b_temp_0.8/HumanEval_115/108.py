
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
    # Find out how many wells we have.
    wells = 0
    for row in grid:
        wells += row.count(1)
    if wells == 0:
        return 0
    # Find out how many wells we need to fill.
    bucket_count = 0
    for row in grid:
        for i, well in enumerate(row):
            if well == 1:
                bucket_count += 1
    # How many times do we need to lower the buckets?
    buckets = math.ceil(bucket_count / wells)
    # Find out how many wells we need to fill.
    wells = 0
    for row in grid:
        wells += row.count(0)
    # Find out how many times we can fill up a well.
    water = 0
    for i in range(wells):
        water += capacity
    # How many times do we need to fill up wells?
    times = math.ceil(wells / buckets)
    return water * times
