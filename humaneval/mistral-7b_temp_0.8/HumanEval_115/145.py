
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
    n, m = grid.shape
    cap = capacity
    # grid size
    g = max(n, m)
    # max number of buckets needed
    if n == g or m == g:
        return g

    # max number of buckets needed
    max_buckets = 2 * g - 2

    # just need 1 bucket
    if cap >= g:
        return 1

    # init bucket count
    buckets = 0

    # main loop
    while True:
        # fill buckets
        grid[0][0] -= cap
        grid[g - 1][g - 1] -= cap

        # fill water in buckets
        for i in range(1, g - 1):
            grid[i][i] += cap

        # fill water in grid
        for i in range(1, g - 1):
            grid[i][0] += cap
            grid[0][i] += cap
            grid[g - 1][i] += cap
            grid[i][g - 1] += cap
