
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
    
    m, n = len(grid), len(grid[0])
    f = [0] * (m + 1)  # f[i] -> lowest index of the last well with capacity i
    g = [0] * (m + 1)  # g[i] -> sum of the first (i - 1) columns in each row
    
    for i in range(m):
        g[i + 1] = g[i] + grid[i][0]
        f[i + 1] = max(f[i] + 1, i + 1)
        for j in range(1, n):
            if grid[i][j] == 1 and f[i] == i:
                f[i] = min(f[i], j + 1)
            g[i] = max(g[i], g[i - 1] + grid[i][j])

    # print(f, g)
    result = 0
    for i in range(m):
        # print(g[i], grid[i][-1
