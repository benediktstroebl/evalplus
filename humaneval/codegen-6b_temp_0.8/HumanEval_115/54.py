
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
    if not grid or not grid[0]:
        return 0
    r = len(grid)
    c = len(grid[0])
    
    # create "grid" with all wells as infinite
    grid = [[math.inf] * c for _ in range(r)]
    
    # fill all the wells
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                break
            
            for row in range(i):
                grid[row][j] = min(grid[row][j], grid[i][j] - 1)
            
            for col in range(j):
                grid[i][col] = min(grid[i][col], grid[i][j] - 1)
            
            grid[i][j] = 0
    
    # count the number of times we need to lower the buckets
    count = 0
    for row in grid:
        for val in row:
            count += val
    
    return count
