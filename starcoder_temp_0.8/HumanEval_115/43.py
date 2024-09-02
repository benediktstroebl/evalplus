
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
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])

    # dp[i][j] stores the maximum number of times we can fill the well with index (i,j)
    # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    # dp[0][j] = max(dp[0][j-1] + grid[0][j], 0)
    # dp[i][0] = max(dp[i-1][0] + grid[i][0], 0)
    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        dp[i][0] = max(dp[i-1][0] + grid[i][0], 0)

    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1] + grid[0][j], 0)

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return math.ceil(capacity / (grid[0][0] + 1)) - 1 - max(dp[-1][-1], capacity)

