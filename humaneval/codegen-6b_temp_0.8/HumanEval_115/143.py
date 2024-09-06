
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
    grid_len = len(grid)
    well_len = len(grid[0])
    
    well_count = 0
    for well_i in range(well_len):
        well_count = well_count + sum(grid[i][well_i] for i in range(grid_len))
    
    # how many buckets can be filled
    bucket_count = well_count / capacity
    
    # how many times we need to use new buckets
    bucket_times_needed = well_count % capacity
    
    # since we have a bucket so we have to sink the wells
    # we need to go over each bucket and sink the wells
    # so increment the count on each bucket
    # if we have to use buckets more than the capacity
    # we push all the wells by 1 bucket in the next run
    count = 0
    while bucket_times_needed > 0:
        for bucket_i, bucket_wells in enumerate(grid):
            for well_j in range(well_len):
                if bucket_wells[well_j] > 0:
                    bucket_wells[well_j] -= 1
                    
        count += 1
        bucket_times_needed = bucket_times_needed - bucket_count

    return count

