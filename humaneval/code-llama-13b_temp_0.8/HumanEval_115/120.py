
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
    rows, columns = len(grid), len(grid[0])
    cells = (rows * columns)
    rows_with_1, cols_with_1 = 0, 0
    for row in grid:
        rows_with_1 += len([x for x in row if x != 0])
    for i in range(columns):
        column = [row[i] for row in grid]
        cols_with_1 += len([x for x in column if x != 0])
    print(rows_with_1)
    print(cols_with_1)
    print(cells)
    rows_w_more_1 = rows_with_1 / rows
    cols_w_more_1 = cols_with_1 / columns
    print(rows_w_more_1)
    print(cols_w_more_1)
    max_water_cells = min(rows_w_more_1, cols_w_more_1)
    water_cells = math.floor(max_water_cells * capacity)
    print(water_cells)
    if water_cells < cells:
        return water_cells
    return cells - 1

