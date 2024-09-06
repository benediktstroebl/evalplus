
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
    total_rows = len(grid)
    if total_rows == 0:
        return 0
    total_cols = len(grid[0])
    if total_cols == 0:
        return 0
    total_buckets = capacity

    empty = [0] * total_cols
    filled = [0] * total_cols
    for row_idx in range(total_rows):
        row = grid[row_idx]
        bucket_idx = 0
        for col_idx in range(total_cols):
            col = row[col_idx]
            if col == 0:
                empty[bucket_idx] += 1
            else:
                filled[bucket_idx] += 1
            bucket_idx += 1
    if sum(empty) == 0:
        return 0
    if sum(filled) == 0:
        return total_buckets * total_rows
    filled_buckets = 0
    empty_buckets = total_buckets
    steps = 0
    filled_to_empty = 0
    while filled_buckets < total_buckets:
        if filled_to_empty < empty_buckets:
            empty_buckets -= filled_to_empty
        else:
            empty_buckets = filled_to_empty
        steps += 1
        # Fill bucket
        filled_buckets += empty_buckets
        # Empty bucket
        filled_to_empty = 0
        for idx in range(total_buckets):
            filled_to_empty += empty[idx]
            empty[idx] = 0
            filled[idx] = 0
    return steps
