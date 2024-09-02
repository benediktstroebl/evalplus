
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
    result = 0
    if not grid:
        return 0
    while grid:
        well = None
        well_index = None
        for i, row in enumerate(grid):
            if well is None or sum(row) > well:
                well = sum(row)
                well_index = i
        if well is None or well == 0:
            return result
        for j in range(len(grid[well_index])):
            if grid[well_index][j] > 0:
                break
        grid[well_index][j] -= 1
        result += math.ceil(well / capacity)
        grid = grid[:well_index] + [[x - (x // capacity * capacity) for x in grid[well_index]]] + grid[well_index+1:]
    return result
