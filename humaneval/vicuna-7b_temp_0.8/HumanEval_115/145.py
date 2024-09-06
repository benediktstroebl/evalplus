
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
    
    n = grid.length
    m = grid[0].length
    filled = [[0] * m for _ in range(n)]
    empty = [[0] * m for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            filled[i][j] = grid[i-1][j-1]
            empty[i][j] = 1
            
    max_val = 0
    for i in range(n):
        for j in range(m):
            if filled[i][j] > max_val:
                max_val = filled[i][j]
            if j > 0 and empty[i][j-1] > 0:
                max_val -= empty[i][j-1]
    
    return max_val
