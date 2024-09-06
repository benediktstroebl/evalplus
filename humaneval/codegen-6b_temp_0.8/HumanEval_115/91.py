
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
    well_length = len(grid[0])
    n_wells = len(grid)

    # init buckets at each well
    buckets = defaultdict(int)
    for well in grid:
        for bucket in well:
            buckets[bucket] += 1

    # track max filling
    max_filled = 0
    for bucket_capacity in range(1, capacity + 1):
        # create buckets
        write = [bucket_capacity for _ in range(well_length)]
        bucket_available = [bucket_capacity for _ in range(well_length)] # able to fill a bucket

        # refill buckets
        for i in range(well_length):
            if buckets[i] > 0:
                write[i] = buckets[i] # refill bucket
                buckets[i] = 0 # empty bucket
                bucket_available[i] -= 1 # bucket_available count

        # fill the wells
        for well in grid:
            if sum(well) <= bucket_capacity:
                for bucket_idx in range(well_length):
                    if bucket_available[bucket_idx] > 0 and write[bucket_idx] > 0:
                        write[bucket_idx] -= 1
                        bucket_available[bucket_idx] -= 1
                    if bucket_available[bucket_idx] == 0:
                        break

        cur_filled = sum(write)
        if cur_filled > max_filled:
            max_filled = cur_filled
        if cur_filled == well_length * bucket_capacity:
            return max_filled
    return max_filled
