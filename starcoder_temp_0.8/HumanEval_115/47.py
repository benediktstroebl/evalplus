
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
    n_buckets = math.ceil(len(grid) * len(grid[0]) / capacity)

    filled_buckets = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                filled_buckets += 1

    # if there is no water in the wells, return 0
    if filled_buckets == 0:
        return 0

    # if there is no more space to fill in the buckets, return 1
    if filled_buckets <= n_buckets:
        return 1

    # if there is enough space to fill in the buckets, return 0
    if filled_buckets % n_buckets == 0:
        return 0

    # if we reach here, we have filled the grid in the number of times
    # that it is not divisible by n_buckets
    return filled_buckets % n_buckets
