
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

    if grid is None or len(grid) == 0:
        return 0
    if capacity is None or capacity <= 0:
        return 0
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    for row in grid:
        if len(row)!= len(grid[0]):
            return "Invalid grid."

    width = len(grid[0])
    height = len(grid)
    bucket_capacity = capacity

    water_per_well = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                water_per_well[i][j] = 0
                continue
            
            if i > 0:
                water_per_well[i][j] += max(0, water_per_well[i-1][j] - 1)
            if j > 0:
                water_per_well[i][j] += max(0, water_per_well[i][j-
