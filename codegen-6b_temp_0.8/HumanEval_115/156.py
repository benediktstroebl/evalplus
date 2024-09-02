
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
    import math
    grid_max = 0
    for row in grid:
        grid_max = max(grid_max, max(row))
    if grid_max * bucket_capacity < capacity:
        return 0
    else:
        grid_copy = list(map(list, zip(*grid)))
        max_grid = 0
        for row in grid_copy:
            max_grid = max(max_grid, max(row))
        filler = math.ceil(capacity / max_grid)
        for row in grid:
            row[:] = [1 - i for i in row]
        for i in range(filler - 1):
            grid = list(map(list, zip(*grid)))
            for row in grid:
                row[:] = [1 - i for i in row]
        return filler - 1
