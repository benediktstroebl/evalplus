
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
    max_level, max_row, max_col = 0, 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                max_level = max(max_level, i)
                max_row = max(max_row, j)
    
    max_level += 1
    max_row += 1
    max_col = capacity

    lowest_level = [math.inf] * max_col
    lowest_level[0] = 0

    for row in range(max_row):
        new_lowest_level = [math.inf] * max_col
        for col in range(max_col):
            level = lowest_level[col]
            if level == math.inf:
                continue
            if row >= max_level:
                new_lowest_level[col] = level
                continue
            new_lowest_level[max(col, grid[level][row] - 1)] = min(lowest_level[max(col, grid[level][row] - 1)], level + 1)
        lowest_level = new_lowest_level

    return lowest_level[-1]

