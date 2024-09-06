
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
    height, width = len(grid), len(grid[0])
    if height == 0 or width == 0 or height > 100 or width > 100:
        return 0
    if capacity > 10:
        return 0

    if height == 1 and width == 1:
        if grid[0][0] == 0:
            return 0
        else:
            return 1

    if height == 1 and width > 1:
        if grid[0][0] == 0:
            return 0
        else:
            return min(width, (grid[0][0] // capacity) + 1)

    if width == 1 and height > 1:
        if grid[0][0] == 0:
            return 0
        else:
            return min(height, (grid[0][0] // capacity) + 1)

    if height > 1 and width > 1:
        possible_grid = [[0] * width for i in range(height)]
        for i in range(height
