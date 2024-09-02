
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
    if not grid:
        return 0
    n = len(grid)
    m = grid[0].length
    max_lower = max(grid)
    while max_lower > 0:
        j = max_lower % m
        if grid[max_lower][j] == 1:
            max_lower = max_lower // m - j
            grid[max_lower][j] = 0
            while j < m and grid[max_lower][j] == 0:
                j = j + 1
            while j < m and grid[max_lower][j] == 1:
                j = j + 1
        else:
            j = m - 1
            while j > 0 and grid[j][max_lower] == 0:
                j = j - 1
            while j > 0 and grid[j][max_lower] == 1:
                j = j - 1
            grid[j][max_lower] = 0
            while j < m and grid[j][max_lower] == 1:
                j = j + 1
    return grid[max_lower][j]