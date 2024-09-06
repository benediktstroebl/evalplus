
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
    if not grid or not grid[0]: return 0
    if not capacity: return 0
    if len(grid) <= 1: return 0

    rows = len(grid)
    if rows == 1:
        for i in grid[0]:
            if i == 1: return 1
        return 0
    if rows == 2:
        if grid[0][0] == 1: return 1
        if grid[1][0] == 1: return 1
        if grid[0][1] == 1: return 1
        return 0

    wells = 0
    for row in grid:
        wells += row.count(1)
    
    max_buckets = capacity // wells

    grid_copy = [row[:] for row in grid]

    grid = [[0 for j in range(len(row))] for i, row in enumerate(grid_copy)]
    grid_copy = [[0 for j in range(len(row))] for i, row in enumerate(grid_copy)]

    # 1. Add the first row, 
    for j in range(len(grid[0])):
        grid[0][j] = 1
        if grid[0][j] == max_buckets: wells += 1
    wells -= 1
    grid[0][0] = 0
    # 2. Remove last column 
    for i in range(1, len(grid)):
        grid[i][-1] = 0
        if grid[i][-1] == max_buckets: wells += 1

    # 3. Remove last row
    for j in reversed(range(1, len(grid[0])-1)):
        grid[-1][j] = 0
        if grid[-1][j] == max_buckets: wells += 1

    # 4. Remove the first column
    for i in range(1, len(grid)-1):
        grid[i][0] = 0
        if grid[i][0] == max_buckets: wells += 1

    # 5. Remove the first row
    for j in reversed(range(1, len(grid[0])-1)):
        grid[0][j] = 0
        if grid[0][j