
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

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    if rows == 1 and cols == 1:
        if grid[0][0] == 1:
            return 0
        else:
            return 1
    
    max_bucket_capacity = capacity
    max_filled_wells = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                filled = 0
                total_filled = 0
                well_positions = []
                buckets_filled = []
                current_well = grid[row][col]
                next_row = row
                next_col = col
                while current_well > 0:
                    filled += 1
                    total_filled += 1
                    well_positions.append((row, col))
                    if next_row < rows-1:
                        next_row += 1
                    else:
                        next_row = 0
                    if
