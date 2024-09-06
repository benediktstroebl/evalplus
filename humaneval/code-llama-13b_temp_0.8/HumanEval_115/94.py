
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
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Horizontal fills
    # For each row, we fill all the buckets until the
    # last filled bucket is on the right
    for row_idx in range(num_rows):
        row = grid[row_idx]
        num_filled = 0
        for col_idx in range(num_cols):
            if row[col_idx] == 1:
                num_filled += 1
            elif row[col_idx] == 0:
                num_filled = 0
            bucket_size = num_filled
            if bucket_size > capacity:
                return -1

    # Vertical fills
    # For each column, we fill all the buckets until the
    # last filled bucket is on the bottom
    for col_idx in range(num_cols):
        col = [grid[i][col_idx] for i in range(num_rows)]
        num_filled = 0
        for row_idx in range(num_rows):
            if col[row_idx] == 1:
                num_filled += 1
            elif col[row_idx] == 0:
                num_filled = 0
            bucket_size = num_filled
            if bucket_size > capacity:
                return -1
    return 0

