
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
    # n = grid.shape[0]
    # m = grid.shape[1]
    # min_well_size = math.ceil(capacity / n)
    # rows_to_fill = []
    # cols_to_fill = []
    # for i in range(n):
    #     if sum(grid[i,:]) < min_well_size:
    #         rows_to_fill.append(i)
    # for j in range(m):
    #     if sum(grid[:,j]) < min_well_size:
    #         cols_to_fill.append(j)
    # n_fills = 0
    # while rows_to_fill or cols_to_fill:
    #     if rows_to_fill:
    #         n_fills += 1
    #         i = rows_to_fill.pop()
    #         grid[i,:] = 1
    #     if cols_to_fill:
    #         n_fills += 1
    #         j = cols_to_fill.pop()
    #         grid[:,j] = 1
    # return n_fills

    n = grid.shape[0]
    m = grid.shape[1]
    min_well_size = math.ceil(capacity / n)
    rows_to_fill = []
    cols_to_fill = []
    for i in range(n):
        if sum(grid[i,:]) < min_well_size:
            rows_to_fill.append(i)
    for j in range(m):
        if sum(grid[:,j]) < min_well_size:
            cols_to_fill.append(j)
    return len(rows_to_fill) + len(cols_to_fill)

