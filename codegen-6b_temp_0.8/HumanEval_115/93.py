
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
    buckets = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                buckets[i][j] = grid[i][j]
    res = 0
    while any(x > 0 for x in buckets[0]):
        if buckets[0][0] <= capacity:
            buckets[0][0] -= 1
            res += 1
        else:
            buckets[0][0] = 0
        del buckets[0][0]
    while any(x > 0 for x in buckets[n-1]):
        if buckets[n - 1][m-1] <= capacity:
            buckets[n-1][m-1] -= 1
            res += 1
        else:
            buckets[n-1][m-1] = 0
        del buckets[n-1][m-1]
    for i in range(1, n - 1):
        while any(x > 0 for x in buckets[i]):
            if buckets[i][0] <= capacity:
                buckets[i][0] -= 1
                res += 1
            else:
                buckets[i][0] = 0
            del buckets[i][0]
    while any(x > 0 for x in buckets[0]):
        if buckets[0][0] <= capacity:
            buckets[0][0] -= 1
            res += 1
        else:
            buckets[0][0] = 0
        del buckets[0][0]
    while any(x > 0 for x in buckets[n-1]):
        if buckets[n-1][m-1] <= capacity:
            buckets[n-1][m-1] -= 1
            res += 1
        else:
            buckets[n-1][m-1] = 0
        del buckets[n-1][m-1]
    return res
