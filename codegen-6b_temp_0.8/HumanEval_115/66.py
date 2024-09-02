
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
    row_len = len(grid)
    col_len = len(grid[0])
    num_wells = sum([sum(row) for row in grid])
    # simple implementation, with n*n naive DP
    # dp_grid = [[[0] * col_len for _ in range(row_len)] for _ in range(num_wells + 1)]
    dp_grid = [[0] * col_len for _ in range(num_wells + 1)]
    dp_grid[0] = [0] * col_len
    for i in range(1, num_wells + 1):
        for j in range(col_len):
            if grid[i - 1][j] == 0:
                continue
            # we consider previous rows not to be given to this well
            dp_grid[i][j] = max(dp_grid[i - 1][k] + grid[i - 1][k] for k in range(j + 1) if k < j) + grid[i - 1][j]
    return num_wells - dp_grid[-1][-1]

