
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
    grid = [int(row) for row in grid]
    rows, cols = grid[0].shape
    row_sums = [sum(row) for row in grid]
    row_sums_max = max(row_sums)
    if row_sums_max > grid[0].size - 1:
        return 0
    else:
        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] == 1:
                    if (i-1 >= 0 and grid[i-1][j] == 0) or (i+1 < rows and grid[i+1][j] == 0):
                        grid[i][j] = 0
                        bucket_index = max_fill(grid, capacity-1) - 1
                        grid[i][j] = 1
                        for k in range(bucket_index, capacity):
                            if grid[i][j-k] == 0 or grid[i-k][j] == 0:
                                grid[i][j] = 0
                                break
    return grid[0].size
