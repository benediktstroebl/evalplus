
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
    """
    # from itertools import accumulate
    # 1) find starting position for bucket
    # 2) fill up bucket to capacity
    # 3) find the max_fill between bucket and the last 1
    # 4) repeat from 1 until grid is empty

    count = 0
    total_filled = 0
    for col_idx in range(len(grid[0])):
        # find starting position for bucket
        start_row_idx = None
        for row_idx in range(len(grid)):
            if grid[row_idx][col_idx] == 1:
                start_row_idx = row_idx
                break
        
        if start_row_idx is None:
            continue
        else:
            # fill up bucket to capacity
            count += 1
            for row_idx in range(start_row_idx, len(grid)):
                if grid[row_idx][col_idx] == 1:
                    grid[row_idx][col_idx] = 0
                    total_filled += 1
                if total_filled == capacity:
                    break
        if total_filled == capacity:
            break
    return count
    """

    total_filled = 0
    count = 0
    while total_filled != capacity * len(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    grid[i][j] = 0
                    if count == capacity:
                        break
            if count == capacity:
                break
        if count == capacity:
            break
    return count
