
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
    # number of buckets
    n_buckets = min(bucket_capacity, len(grid))
    # the maximum number of times you can lower the buckets
    max_bucket_lower = math.ceil(sum([sum(row) for row in grid]) / n_buckets)
    # the number of buckets you need to empty the wells
    n_bucket_lower = 0
    # the number of empty wells
    n_empty_wells = 0
    # the number of times you need to lower the buckets
    n_bucket_lower = 0
    # number of times the last bucket was lowered
    last_bucket_lowered = 0

    for bucket_lower in range(max_bucket_lower):
        for bucket in range(n_buckets):
            for well in range(len(grid)):
                if grid[well][bucket] == 1:
                    grid[well][bucket] = 0
                    n_empty_wells += 1
                    if n_empty_wells == len(grid):
                        return n_bucket_lower
            n_bucket_lower += 1
            last_bucket_lowered += 1
            if last_bucket_lowered == n_buckets:
                return max_bucket_lower
    return max_bucket_lower
