
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
    rows, cols = grid.shape
    if not grid:
        return 0
    if rows == 0 or cols == 0:
        return 0
    if not (0 <= grid[0][0] <= rows - 1 and 0 <= grid[0][0] < grid[0][0]):
        return 0

    if (1 <= grid[0][0] <= rows - 1 and 0 <= grid[0][0] < grid[0][0]):
        min_fill = grid[0][0]
        for i in range(1, rows - 1):
            if grid[i][0] < min_fill:
                min_fill = grid[i][0]
        return min_fill

    if (0 <= grid[0][0] <= cols - 1 and 0 <= grid[0][0] < grid[0][0]):
        min_fill = grid[0][0]
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] < min_fill:
                    min_fill = grid[i][j]
        return min_fill

    return 0