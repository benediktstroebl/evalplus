
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
    if capacity == 0:
        return 0

    r = len(grid)
    c = len(grid[0])
    p = 0
    while p < r:
        l = 0
        while l < c:
            if grid[p][l] == 0:
                l += 1
            else:
                grid[p][l] = 0
                while l < c and grid[p][l] == 1:
                    l += 1
                # do not move pointer if already at the end
                if l < c:
                    # remove bucket from previous column
                    grid[p][l-1] = 1
                    # fill the buckets in between
                    for i in range(p+1, r):
                        grid[i][l] = 0
                        for j in range(l+1, c):
                            if grid[i][j] == 1:
                                grid[i][j] = 0
                                break
                    p += 1
        p += 1
    return p

