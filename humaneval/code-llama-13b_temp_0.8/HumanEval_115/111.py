
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
    num_buckets = capacity
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_fills = 0
    row_idx = 0
    col_idx = num_cols - 1
    row_idxs = list(range(num_rows))
    col_idxs = list(range(num_cols))
    while row_idx < num_rows and col_idx >= 0:
        fill_amount = min(num_buckets, int(math.ceil(num_buckets / (num_rows - row_idx))))
        num_fills += fill_amount
        num_buckets -= fill_amount
        for i in range(fill_amount):
            grid[row_idx][col_idx] = 0
        for i in range(fill_amount):
            while col_idx >= 0 and grid[row_idx][col_idx] == 0:
                col_idx -= 1
            if col_idx < 0:
                break
            for j in range(row_idx, num_rows):
                if grid[j][col_idx] == 1:
                    grid[j][col_idx] = 0
                    row_idx = max(row_idx, j)
                if j == num_rows - 1:
                    col_idx -= 1
        row_idx += 1
    return num_fills

