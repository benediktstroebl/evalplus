
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

    well_count = len(grid)
    bucket_count = len(grid[0])
    buckets = [[capacity for i in range(bucket_count)] for j in range(well_count)]
    grid = [list(i) for i in grid]
    for i in range(well_count):
        for j in range(bucket_count):
            if grid[i][j] == 1:
                buckets[i][j] -= 1
                if buckets[i][j] == 0:
                    grid[i][j] = 0
    
    while any(1 in i for i in grid):
        s = [i.count(1) for i in grid]
        if not all(i == 0 for i in s):
            max_i = s.index(max(s))
            max_j = s[max_i].index(max(s[max_i]))
            grid[max_i][max_j] = 0
            buckets[max_i][max_j] += 1
            if buckets[max_i][max_j] > capacity
