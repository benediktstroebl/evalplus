
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
    n_rows, n_columns = len(grid), len(grid[0])
    n_wells = sum(grid[0])
    # If we can fill the buckets with every well we have, then the number
    # of operations needed will be the number of wells.
    if n_wells <= capacity:
        return n_wells

    max_row_buckets = [0] * n_rows
    max_column_buckets = [0] * n_columns
    # Fill each column in the grid
    for col in range(n_columns):
        # Find the max bucket height from the current column
        max_bucket = 0
        for row in range(n_rows):
            if grid[row][col] == 1:
                max_bucket = max(max_bucket, max_row_buckets[row])
        # Update the max column bucket if the max bucket is larger than
        # the current bucket height
        if max_bucket > max_column_buckets[col]:
            max_column_buckets[col] = max_bucket
    # Fill each row in the grid
    for row in range(n_rows):
        # Find the max bucket height from the current row
        max_bucket = 0
        for col in range(n_columns):
            if grid[row][col] == 1:
                max_bucket = max(max_bucket, max_column_buckets[col])
        # Update the max row bucket if the max bucket is larger than
        # the current bucket height
        if max_bucket > max_row_buckets[row]:
            max_row_buckets[row] = max_bucket
    # The number of operations needed will be the number of rows with non-zero
    # heights minus the number of rows with zero heights.
    return math.ceil(n_wells / capacity) - len(
        [True for bucket in max_row_buckets if bucket == 0])

