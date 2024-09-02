
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

    if capacity < 1: return 0

    n = len(grid)
    m = len(grid[0])
    if n == 0 or m == 0: return 0

    g = [[math.inf]*m for i in range(n)]
    b = [[math.inf]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            g[i][j] = 1 if grid[i][j] == 1 else 0

    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                for dx, dy in [[0,0], [0,1], [1,0], [1,1]]:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and x < n and y >= 0 and y < m:
                        g[i][j] = min(g[i][j], g[x][y] + 1)
                        b[i][j] = min(g[i][j], b[x][y])
    
