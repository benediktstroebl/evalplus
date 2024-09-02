
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
    # DP[i][j] -> the minimum number of times we need to lower the buckets to empty the column from i to j
    # DP[i][j] = min{ DP[i][j], DP[i-1][k-1] + DP[k+1][j] }
    # DP[i][j] = min{ DP[i][j], DP[i-1][k] + DP[k+1][j] }
    # DP[i][j] = min{ DP[i][j], DP[i-1][k] + DP[k+1][j] }
    # DP[i][j] = min{ DP[i][j], DP[i-1][k-1] + DP[k+1][j] }
    # DP[i][j] = min{ DP[i][j], DP[i-1][k-1] + DP[k+1][j] }
    # 0 <= i <= j
    # 0 <= k < i
    # k < i
    # k > j

    # 1. Init: 
    #    DP[i][i] = 0
    #    DP[i][i+1] = grid[i][i+1]
    #    DP[i][i-1] = grid[i][i-1]
    # 2. Loop:
    #    DP[i][j] = min{ DP[i][j], DP[i-1][k-1] + DP[k+1][j] }
    # 3. Result:
    #    result = DP[0][n-1]

    n = len(grid[0])
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(1, n):
        dp[0][i] = grid[0][i]
    for i in range(1, n):
        dp[i][i] = 0
    for i in
