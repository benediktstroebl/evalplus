
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

    bucket_capacity = capacity
    row_count = len(grid)
    col_count = len(grid[0])
    bucket_count = math.floor(row_count / 2)
    dp = [[0 for i in range(bucket_count + 1)] for j in range(col_count + 1)]
    for j in range(col_count):
        for i in range(row_count):
            if j == 0 and i == 0:
                dp[j][i] = 0
            elif j == 0 and i!= 0:
                dp[j][i] = dp[j][i - 1] + grid[i][j]
            elif j!= 0 and i == 0:
                dp[j][i] = dp[j - 1][i] + grid[i][j]
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1]) + grid[i][j]
            dp[j][i] = max(dp[j][i], bucket_capacity - dp[j
