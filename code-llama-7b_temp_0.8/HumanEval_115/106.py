
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

    rows = len(grid)
    cols = len(grid[0])

    n_buckets = rows
    # Init n_buckets with 1 (at least one bucket).
    # Each bucket will hold capacity water units.
    buckets = [capacity] * n_buckets

    n_times = 0
    total_water = 0
    while True:
        total_water_before_filling = total_water
        # Fill buckets.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    buckets[i] += 1
                    total_water += 1

        # Empty buckets.
        for j in range(cols):
            bucket_total_water = 0
            for i in range(rows):
                bucket_total_water += buckets[i]
            if bucket_total_water > 0:
                # Fill bucket.
                if bucket_total_water > buckets[0]:
                    # Fill with capacity.
                    buckets[0] = buckets[0] + buckets[0] // bucket_total_water * bucket_total_water
                    # Empty overflow.
                    buckets[0] = buckets[0] % bucket_total_water
                    # Empty bucket.
                    for i in range(rows):
                        if buckets[i] > 0:
                            buckets[i] = 0
                else:
                    # Empty bucket.
                    for i in range(rows):
                        if buckets[i] > 0:
                            buckets[i] = 0
                            break

        total_water_after_filling = total_water
        if total_water_after_filling > total_water_before_filling:
            n_times += 1
        else:
            break

    return n_times

