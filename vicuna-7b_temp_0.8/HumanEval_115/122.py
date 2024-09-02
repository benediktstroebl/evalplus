
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

    rows, cols = grid.shape

    # store the minimum for each row
    min_fill_row = [math.inf for _ in range(cols)]

    # store the maximum for each column
    max_fill_col = [0 for _ in range(rows)]

    for row in range(1, rows):
        min_fill_row[row-1] = min(min_fill_row[row-1], grid[row-1][cols-1] + bucket_capacity)

    for col in range(1, cols):
        max_fill_col[0] = max(max_fill_col[0], grid[0][col] + bucket_capacity)

    for row in range(1, rows):
        for col in range(1, cols):
            if grid[row-1][col-1] == 1:
                max_fill_col[0] = max(max_fill_col[0], max_fill_col[col-1])
            if grid[row-1][col] == 1:
                max_fill_col[col] = max(max_fill_col[col], max_fill_col[col-1])
            if grid[row-1][col+1] == 1:
                max_fill_col[col+1] = max(max_fill_col[col+1], max_fill_col[col])
            if grid[row][col-1] == 1:
                max_fill_col[col] = max(max_fill_col[col], max_fill_col[col-1])

    return min_fill_row[-1]