
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
    grid = list(grid)
    rows = len(grid)
    for i in range(1, rows):
        for j in range(1, rows):
            if grid[i][j] == 1:
                for k in range(0, j-1):
                    for l in range(0, i-1):
                        if grid[l][k] == 1 and grid[i][j] != 1:
                            grid[l][k], grid[i][j] = grid[i][j], grid[l][k]
                            capacity -= 1
                            if capacity == 0:
                                break
                    if capacity == 0:
                        break
    return grid[0][0]