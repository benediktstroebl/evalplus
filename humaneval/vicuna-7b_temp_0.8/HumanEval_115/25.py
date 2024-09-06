
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

    if grid.length == 0 or grid.length == 1:
        return 0
    if grid.length == 2:
        return 1
    
    for i in range(0, grid.length - 1):
        if grid[i][0] == 1 and grid[i+1][0] == 1:
            return max([max_fill(grid, capacity-1), max_fill(grid, capacity)])
        elif grid[i][0] == 1:
            return max_fill(grid, capacity-1)
        elif grid[i+1][0] == 1:
            return max_fill(grid, capacity)
        
    return max_fill(grid, capacity)
