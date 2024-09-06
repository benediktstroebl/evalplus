
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
    if not grid or not grid[0]: return 0
    max_row = len(grid)
    max_col = len(grid[0])
    num_fills = 0
    while True:
        filled_wells = []
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if not col: continue
                if row_idx in filled_wells or col_idx in filled_wells: continue
                if 0 < col < capacity:
                    grid[row_idx][col_idx] = 0
                    num_fills += 1
                    filled_wells.extend([row_idx, col_idx])
        if not filled_wells: break
    return num_fills

