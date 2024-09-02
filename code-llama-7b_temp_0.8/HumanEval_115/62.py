
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
    assert grid
    assert len(grid) == len(grid[0])
    assert len(grid) > 0
    assert len(grid[0]) > 0

    # Handle empty wells
    if capacity == 0:
        return 0

    # Handle unachievable capacity
    if capacity >= len(grid):
        return len(grid)

    # Initialize variables
    num_wells = len(grid)
    num_wells_rows = len(grid[0])
    bucket_capacity = capacity

    # Initialize buckets
    num_buckets = num_wells
    buckets = [bucket_capacity] * num_buckets

    # Initialize wells
    wells = []
    for row in grid:
        well = []
        for col in row:
            well.append(col)
        wells.append(well)

    # Initialize times bucket is lowered
    times_bucket_lowered = 0

    # Empty wells
    while wells:
        well = wells.pop(0)
        bucket_capacity = buckets.pop(0)
        if well:
            # Remove water from the well
            water_removed = well.pop(0)

            # if water can't be removed from well, add it to bucket
            # and add one to times bucket is lowered
            if water_removed == 0:
                bucket_capacity += water_removed
                times_bucket_lowered += 1
            # else, if water can be removed from well, add it to bucket
            # and add one to times bucket is lowered if bucket capacity
            # is full
            else:
                bucket_capacity += water_removed
                if bucket_capacity == bucket_capacity:
                    times_bucket_lowered += 1

    # Return times bucket was lowered
    return times_bucket_lowered
