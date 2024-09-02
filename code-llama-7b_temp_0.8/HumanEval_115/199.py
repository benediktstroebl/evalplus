
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
    n_rows = len(grid)
    n_cols = len(grid[0])
    bucket_capacity = capacity
    total_units = sum([sum(row) for row in grid])
    n_buckets = n_rows + 1
    water_per_bucket = bucket_capacity
    buckets = [water_per_bucket for _ in range(n_buckets)]

    # should be O(n_rows * n_cols)
    for i in range(n_rows):
        for j in range(n_cols):
            buckets[i] -= grid[i][j]
            buckets[i + 1] += grid[i][j]
    total_buckets = sum(buckets)

    if total_units <= bucket_capacity:
        return 0

    n_lowered = math.floor(total_units / bucket_capacity)
    n_lowered -= total_buckets
    return n_lowered

