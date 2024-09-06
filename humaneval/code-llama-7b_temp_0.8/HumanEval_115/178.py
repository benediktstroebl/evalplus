
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
    n_wells = len(grid)
    n_buckets = 1
    # Number of times the buckets need to be lowered
    times_buckets_lowered = 0
    # Last well watered
    last_well_watered = None
    # Number of wells watered in a row
    n_wells_watered_in_row = 0
    # Number of wells filled
    n_wells_filled = 0
    # Number of wells emptied
    n_wells_emptied = 0
    # Bucket capacity
    bucket_capacity = capacity
    #
    # Iterate over all rows in grid
    #
    for i, wells in enumerate(grid):
        # Iterate over all columns in row
        for j, well in enumerate(wells):
            if well:
                n_wells_watered_in_row += 1
                # If the well is watered and
                # the bucket is empty,
                # lower the bucket
                if not last_well_watered:
                    last_well_watered = well
                    times_buckets_lowered += 1
            else:
                # If the well is dry and
                # the bucket is full,
                # empty the bucket
                if last_well_watered:
                    n_wells_emptied += 1
                    if n_wells_emptied == bucket_capacity:
                        # If the bucket is full and
                        # there are still empty wells,
                        # increment the number of buckets
                        n_buckets += 1
                    last_well_watered = None
                    n_wells_emptied = 0

        # If the bucket is empty,
        # lower the bucket
        if last_well_watered:
            times_buckets_lowered += 1
            last_well_watered = None

        # If there are still empty wells
        # after the row,
        # lower the bucket
        if n_wells_watered_in_row < n_wells:
            times_buckets_lowered += 1
