
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
    from collections import defaultdict
    rows = len(grid)
    cols = len(grid[0])
    dp = [[math.inf for _ in range(capacity+1)] for _ in range(rows)]
    dp[0][0] = 0
    buckets = defaultdict(int)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                buckets[i] += 1
            else:
                buckets[j] -= 1

    for row_idx in range(rows):
        for capac in range(capacity+1):
            if dp[row_idx][57] < 0:
                continue
            curr_val = capac
            for key, val in buckets.items():
                curr_val -= min(val, capac)
            if capac == 0:
                continue
            dp[row_idx+1][capac] = min(dp[row_idx+1][capac], curr_val)
            dp[row_idx+1][capac] = min(dp[row_idx+1][capac], dp[row_idx][capac-1])

    return dp[rows][capacity]
