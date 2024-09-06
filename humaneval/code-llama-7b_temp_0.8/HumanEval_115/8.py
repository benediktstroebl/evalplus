
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
    # Validate and initialize input
    n_rows = len(grid)
    n_cols = len(grid[0])
    total_buckets = n_rows + n_cols

    # Calculate the number of water buckets that can be used to empty the wells
    # Determine the number of times the buckets need to be lowered
    num_buckets_used = 0
    num_lowers = 0
    while num_buckets_used < total_buckets:
        # Determine the number of buckets needed to fill all the wells
        for row in range(n_rows):
            if sum(grid[row]) < capacity:
                num_buckets_used += 1

        # Lower the buckets to empty all the wells
        for row in range(n_rows):
            if sum(grid[row]) < capacity:
                for col in range(n_cols):
                    if grid[row][col] == 1:
                        grid[row][col] = 0
                        num_lowers += 1
                        if num_buckets_used == total_buckets:
                            break

        # Determine the number of buckets needed to fill all the wells
        for col in range(n_cols):
            if sum(grid[:,col]) < capacity:
                num_buckets_used += 1

        # Lower the buckets to empty all the wells
        for col in range(n_cols):
            if sum(grid[:,col]) < capacity:
                for row in range(n_rows):
                    if grid[row][col] == 1:
                        grid[row][col] = 0
                        num_lowers += 1
                        if num_buckets_used == total_buckets:
                            break

    return num_lowers


