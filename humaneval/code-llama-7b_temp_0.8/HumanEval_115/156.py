
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
    # estimate the number of times the buckets need to be lowered
    num_wells = len(grid)
    max_water = 0
    num_lowers = 0
    # started with the first well, and each time we lower the bucket, we need to
    # move to the right to find a new well to lower into
    # this way, we don't need to search the whole array
    # it's enough to move to the right to find a new well
    # then after we've lowered into the well, we don't need to move back to the left
    well_idx = 0
    for well_idx in range(len(grid)):
        # get the current well
        well = grid[well_idx]
        # get the water in the well
        water = 0
        for unit in well:
            if unit:
                water += unit
        # if there's more water than we can hold, we need to lower the bucket once
        # because it needs to be lowered into a new well
        if water > capacity:
            num_lowers += 1
        # update the max_water
        max_water = max(max_water, water)

    # update the max_water
    # make sure we've filled up all wells that we could
    max_water = max(max_water, capacity * num_wells)

    # calculate the number of buckets we need to lower
    # max_water / capacity + 1 -> max_water / capacity: num_buckets
    # max_water / capacity + 1 -> ceil(max_water / capacity): num_buckets + 1
    # ceil(max_water / capacity) - 1: num_buckets
    # max_water / capacity: num_buckets
    # max_water / capacity - 1: num_buckets - 1
    num_buckets = max_water // capacity
    # the extra 1 is because the first lower needs to be accounted for
    num_buckets += 1
    # but since we're counting the number of times we need to lower the bucket,
    # we need to subtract 1 because the first lower isn
