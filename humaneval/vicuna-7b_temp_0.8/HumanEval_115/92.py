
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
    min_times = math.inf
    for i in range(grid.length):
        for j in range(grid[0].length):
            for k in range(grid[0].length):
                if grid[i][j] == 1 and grid[i][k] == 1 and grid[j][k] == 1:
                    if grid[i][j] == 1:
                        if max(grid[i+1][j]) > 0:
                            times = max(1, grid[i+1][j] - grid[i][j])
                            if times > min_times:
                                min_times = times
                        if max(grid[i][j+1]) > 0:
                            times = max(1, grid[i][j+1] - grid[i][j])
                            if times > min_times:
                                min_times = times
                        if max(grid[j+1][k]) > 0:
                            times = max(1, grid[j+1][k] - grid[j][k])
                            if times > min_times:
                                min_times = times
    return min_times