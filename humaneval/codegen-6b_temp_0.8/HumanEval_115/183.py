
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
    
    # 1. get per-column max capacity for each buckets
    max_cap = [0] * cols
    for col in range(cols):
        max_cap[col] = max(grid[row][col] for row in range(rows))
    
    # 2. get all the buckets filled per bucket_capacity
    def is_filled(x, y):
        return grid[y][x] == 1
    
    total = rows * cols
    count = 0
    for row in range(rows):
        for col in range(cols):
            if is_filled(col, row):
                continue
            
            # find the largest bucket that can store this bucket
            # if bucket_capacity > max(max_cap[col:col+bucket_capacity]),
            # can still store it
            # -> add 1 to count
            if grid[row][col] == 0:
                for bucket_cap in range(bucket_capacity, 0, -1):
                    if max_cap[col] >= bucket_cap:
                        count += 1
                        break
    
    return count

