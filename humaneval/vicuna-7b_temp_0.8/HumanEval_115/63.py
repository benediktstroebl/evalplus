
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
    min_length = max(grid.shape)
    row_sum = grid[:,0].sum()
    col_sum = grid[:0,1].sum()
    if row_sum == 1:
        if col_sum > 0:
            max_fill_grid(grid, capacity, 0, col_sum - 1)
        else:
            max_fill_grid(grid, capacity, 0, row_sum)
    elif row_sum == 0:
        if col_sum > 0:
            max_fill_grid(grid, capacity, col_sum - 1, row_sum)
        else:
            max_fill_grid(grid, capacity, 0, row_sum)
    else:
        for i in range(1, min_length):
            for j in range(1, min_length):
                if grid[i][j] == 1:
                    fill_grid(grid, capacity, i, j)
                    if grid[i][j] == 1:
                        max_fill_grid(grid, capacity, i, j)
