
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
    # dp[i][j][k] is the minimum number of times we need to lower the buckets
    # to empty the well at (i,j) using the bucket at (k)
    dp = [[[10**9] * (grid.shape[0]) for _ in range(grid.shape[0])] for _ in range(grid.shape[1])]
    dp[0][0][:] = [0] * (grid.shape[1])
    for i in range(1, grid.shape[0]):
        for j in range(1, grid.shape[1]):
            dp[i][j][:] = [0] * (grid.shape[0] - i + 1)
            for k in range(1, grid.shape[1]):
                dp[i][j][k] = min(dp[i][j][k], 
                                  dp[i - 1][j][k] + dp[i][j - 1][k] + dp[i - 1][j - 1][k])
    return dp[grid.shape[0] - 1][grid.shape[1] - 1][:]