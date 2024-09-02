
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

    
    rows = len(grid)
    cols = len(grid[0])
    if rows == 0 or cols == 0:
        return 0
    grid = [[0]+ row+ [0] for row in grid]
    grid = [[0] * (cols+1)] + grid + [[0] * (cols+1)]
    
    def get_bottleneck(grid, col):
        up, down = 0, 0
        if col == 0:
            return math.inf
        for row in range(rows+2):
            if grid[row][col] == 1:
                up = row
                break
        for row in reversed(range(up)):
            if grid[row][col] == 1:
                down = row
                break
        return down - up + 1
    
    def get_left_bottleneck(grid, row):
        left, right = 0, 0
        if row == 0:
            return math.inf
        for col in range(cols+2):
            if grid[row][col] == 1:
                left = col
                
