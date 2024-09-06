
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
    max_water, i, j = 0, 0, 0
    while i < len(grid):
        if grid[i][j] != 0:
            j += 1
        else:
            start = i + 1
            while j < len(grid[i]) and grid[i][j] == 0:
                j += 1
            end = i + 1
            while end < len(grid) and grid[end][j] != 0:
                end += 1
            if end < len(grid):
                end -= 1
            max_water += min(grid[start-1][j], math.ceil((end - start + 1)/capacity)) * capacity
            j += 1
        if j == len(grid[i]):
            i += 1
            j = 0
    return max_water

