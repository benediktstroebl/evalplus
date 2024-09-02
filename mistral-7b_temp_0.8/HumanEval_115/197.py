
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
    # 1. Logic:
    #    - We start at the top left corner of the grid
    #    - For each cell, we try to empty it with the capacity of the bucket
    #    - If we can't empty it, we check the adjacent cells
    #    - We keep going until we can't find an empty cell anymore
    #    - We return the number of times we emptied the wells

    # 2. Algorithm:
    #    - We keep going until we can't find an empty cell anymore
    #    - For each cell, we check the adjacent cells and try to empty them
    #    - If we can't empty the cell, we move to the next cell
    #    - If we can empty the cell, we subtract the number of empty cells from the capacity of the bucket
    #    - If we can't find an empty cell anymore, we return the number of times we emptied the wells
    #    - If we can find an empty cell, we keep going until we can't find an empty cell anymore

    # 3. Code:
    #   
