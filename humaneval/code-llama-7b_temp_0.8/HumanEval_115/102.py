
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
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    # dp[i][j] -> number of times to get water from wells[i][j]
    dp = [[float('inf') for _ in range(n + 1)] for _ in range(m)]
    dp[0][0] = 0

    for i in range(m):
        for j in range(n):
            for k in range(m):
                for l in range(n):
                    if grid[k][l] == 1 and (k != i or l != j):
                        dp[i][j] = min(dp[i][j], dp[k][l] + 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and dp[i][j] != float('inf'):
                return math.ceil(dp[i][j] / capacity)

    return 0
