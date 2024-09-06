
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
    bucket_capacity = capacity
    wells_per_row = len(grid[0])
    wells_per_col = len(grid)
    num_wells = wells_per_col * wells_per_row
    total_filled = 0
    num_fills = 0

    while total_filled < num_wells:
        if (total_filled + wells_per_row) <= num_wells:
            total_filled += wells_per_row
            num_fills += 1
            continue
        elif total_filled + wells_per_col <= num_wells:
            total_filled += wells_per_col
            num_fills += 1
            continue
        else:
            break
    
    return num_fills
