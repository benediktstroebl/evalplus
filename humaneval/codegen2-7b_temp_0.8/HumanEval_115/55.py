
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
    m, n = len(grid), len(grid[0])
    min_bucket = capacity * 2
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                for k in range(min_bucket, capacity + 1):
                    if i - k >= 0 and grid[i - k][j] > 0:
                        grid[i - k][j] -= 1
                    if j - k >= 0 and grid[i][j - k] > 0:
                        grid[i][j - k] -= 1
                min_bucket = 1

    return sum(g == 0 for g in grid[0
