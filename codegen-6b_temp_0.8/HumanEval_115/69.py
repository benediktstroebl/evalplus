
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
    n = len(grid)
    # we should track the max_level and the highest level we could reach at a time
    max_level = max(max(row) for row in grid)
    dp = [[0]*(max_level+1) for _ in range(n)]
    # always reach the maximum level
    for row in grid:
        for i in range(len(row)):
            dp[i][row[i]] += 1
    # any level i could reach at time t is the maximum level at that point
    # max_level = max(max(row) for row in grid)
    # dp[t][i] = max_level
    # print(dp)
    for i in range(1, n):
        for j in range(1, max_level):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            if dp[i][j] > capacity:
                return i
    return 0

