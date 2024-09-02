
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
    n = len(grid)
    m = len(grid[0])
    
    # keep track of the water in the bucket (running max)
    running_max = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # this is the running max
            running_max[i][j] = max(grid[i][j], running_max[i][j])

    # if a well is not full and the bucket is not empty, then we need to lower the bucket's water.
    result = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and running_max[i][j] > 0:
                result += 1
            # we need to reset the bucket to 0, so that we can keep track of the next max
            running_max[i][j] -= grid[i][j]
    return result
