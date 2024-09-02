
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
    # check validity of input
    m, n = len(grid), len(grid[0])
    if m != len(grid[0]) or n != len(grid):
        return -1
    for row in grid:
        if len(row) != n:
            return -1

    # fill all wells in a column with the maximum capacity
    for j in range(n):
        for i in range(m):
            if grid[i][j]:
                fill_well(grid, i, j, capacity)

    # count the number of times you need to lower the buckets
    count = 0
    for row in grid:
        for well in row:
            if well:
                count += 1
    return count

