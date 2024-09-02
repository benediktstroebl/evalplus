
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
    grid_width, grid_height = grid.shape
    max_fill_index = 0
    for i in range(grid_width):
        for j in range(grid_height):
            if grid[i][j] == 1:
                if grid[i][j-1] == 1:
                    if grid[i][j-1] != 0 and grid[i][j-2] == 1:
                        max_fill_index = max(max_fill_index, i+j-2)
                    elif grid[i-1][j] == 1:
                        max_fill_index = max(max_fill_index, i-1)
                if grid[i+1][j] == 1:
                    if grid[i+1][j-1] != 0 and grid[i+1][j-2] == 1:
                        max_fill_index = max(max_fill_index, i+j-2)
                if grid[i+2][j] == 1:
                    if grid[i+2][j-1] != 0 and grid[i+2][j-2] == 1:
                        max_fill_index = max(max_fill_index, i+j-2)
    return max_fill_index