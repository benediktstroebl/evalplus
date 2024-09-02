
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
    from functools import reduce
    if grid == None or len(grid) == 0:
        return 0

    M, N = len(grid), len(grid[0])
    water_cap = capacity
    # water_cap = reduce(lambda x, y: x*y, grid[0])

    # '0' is water, '1' is empty place
    # i, j is the index of bucket
    # transfrom all water to 1
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:
                grid[i][j] = 1

    # count_of_bucket = 0
    count_of_bucket = 1
    count_of_put = 0
    while water_cap > 0:
        count_of_put += 1
        # i, j is the index of wells
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    water_cap -= 1
                    grid[i][j] = 1
        count_of_bucket += 1

    return count_of_put
