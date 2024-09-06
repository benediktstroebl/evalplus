
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
    # write your code here

    wells = 0
    water = 0
    buckets = 0
    for row in grid:
        for bucket in row:
            if bucket == 1:
                wells += 1

    # no need to empty the wells
    if capacity >= wells:
        return 0

    # start with an empty bucket
    buckets = 1

    # for each row in grid
    for row in grid:
        # empty the buckets in the current row
        for bucket in row:
            if bucket == 1:
                buckets += 1
        # extract the amount of water in the row
        water += buckets * capacity
        # the capacity for the next row
        capacity = math.ceil(water / wells)

        # check if the water capacity is reached
        if water >= wells * capacity:
            return buckets

    return buckets

