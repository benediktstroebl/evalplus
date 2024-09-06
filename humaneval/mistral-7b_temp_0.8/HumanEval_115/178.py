
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
    ROW, COL = len(grid), len(grid[0])
    dp = [[0] * COL for _ in range(ROW)]

    for i in range(ROW):
        for j in range(COL):
            if grid[i][j] == 1:
                dp[i][j] = 1
                # if (i, j) is on the edge
                if i == 0 or i == ROW - 1 or j == 0 or j == COL - 1:
                    continue
                # if (i, j) is not on the edge
                else:
                    # up
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j]
                    # down
                    if i + 1 < ROW:
                        dp[i][j] += dp[i + 1][j]
                    # left
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j - 1]
                    # right
