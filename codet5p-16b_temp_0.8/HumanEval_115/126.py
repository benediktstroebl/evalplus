
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

    def _get_row_len(row):
        n = 0
        for num in row:
            if num == 1:
                n += 1
            else:
                break
        return n
    
    if capacity == 0:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    max_fill_rows = 0
    for row in grid:
        max_fill_rows = max(max_fill_rows, _get_row_len(row))

    total_fill_rows = 0
    for row in grid:
        total_fill_rows += _get_row_len(row)
    
    if total_fill_rows == max_fill_rows:
        return math.ceil(total_fill_rows/max_fill_rows)

    max_fill_cols = 0
    for col in range(cols):
        max_fill_cols = max(max_fill_cols, _get_row_len(grid[i][col] for i in range(rows)))

    total_fill_cols =
