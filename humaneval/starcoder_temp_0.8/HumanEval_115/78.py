
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
    m, n = len(grid), len(grid[0])
    p, q = 0, 0
    # init max_fill for each column and each row
    max_fill_for_col = [0] * n
    max_fill_for_row = [0] * m
    for col in range(n):
        for row in range(m):
            if grid[row][col] == 1:
                max_fill_for_row[row] = max(max_fill_for_row[row], 1)
                max_fill_for_col[col] = max(max_fill_for_col[col], 1)
    # init p, q
    for row in range(m):
        p += max_fill_for_row[row]
    for col in range(n):
        q += max_fill_for_col[col]
    # get the minimum number of operation required
    return math.ceil((m*n) / capacity) - (p + q)

