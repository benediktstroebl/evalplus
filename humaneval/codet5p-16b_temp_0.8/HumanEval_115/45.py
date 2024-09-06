
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

    n_row = len(grid)
    n_col = len(grid[0])
    count = 0
    for i in range(n_row):
        for j in range(n_col):
            if grid[i][j] == 1:
                min_count = math.inf
                bucket = bucket_capacity
                while bucket > 0:
                    count += 1
                    for k in range(n_col):
                        if grid[i][k] == 0:
                            min_count = min(min_count, 1 + grid[i][k])
                    bucket -= 1
                    grid[i][j] -= min_count
                    grid[i][j] = max(grid[i][j], 0)
                    if grid[i][j] == 0:
                        break
                    min_count = math.inf
    return count

