
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
    if capacity == 0:
        return 0

    def upper(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return 0
        return grid[i][j]

    def lower(i, j):
        nonlocal buckets
        if i < 0 or j < 0 or i >= n or j >= m:
            return 0
        if grid[i][j] == 0:
            return 0

        if buckets[i][j] > 0:
            return buckets[i][j]
        
        min_low = math.inf
        for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            min_low = min(min_low, lower(i+x, j+y))
        
        buckets[i][j] = min_low + 1
        return buckets[i][j]

    buckets = [[0 for j in range(m)] for i in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if upper(i, j) == 0:
                res = max(res, lower(i, j))
    return res
