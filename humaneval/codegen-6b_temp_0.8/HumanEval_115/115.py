
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
    
    grid_size = len(grid)
    # grid_size is the width of the grid
    # grid[0] is the height of the grid
    cap = capacity
    
    for h in range(grid_size):
        for w in range(grid_size):
            if grid[h][w] == 1:
                for i in range(w - grid_size, w + grid_size):
                    if i < 0 or i >= grid_size:
                        continue
                    cap -= grid[i][w]
                    if cap < 0:
                        return cap
                for j in range(h - grid_size, h + grid_size):
                    if j < 0 or j >= grid_size:
                        continue
                    cap -= grid[h][j]
                    if cap < 0:
                        return cap
    return cap
