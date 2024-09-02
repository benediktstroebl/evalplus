
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

    rows = len(grid)
    cols = len(grid[0])
    bucket_capacity = capacity

    if rows == 0 or cols == 0:
        return 0

    left_bound = 1
    right_bound = math.inf
    dp = [[[0, 0] for _ in range(cols + 1)] for _ in range(rows + 1)]
    dp[1][1][0] = 0
    dp[1][1][1] = 1
    for i in range(1, rows + 1):
        for j in range(left_bound, right_bound + 1):
            if grid[i - 1][j - 1] == 1:
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0], dp[i - 1][j][1]) + 1
                dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][0], dp[i][j - 1][1], dp[i - 1][j - 1][
