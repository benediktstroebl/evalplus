
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
    grid = [int(row) for row in grid]
    capacity_sum = sum(capacity)
    min_len = max(grid)
    min_len = max(grid)
    empty = [0] * min_len
    filled = [0] * min_len
    dp = [[0] * min_len for _ in range(min_len)]
    for i in range(min_len):
        dp[i][0] = i
    for j in range(min_len):
        dp[0][j] = j
    for i in range(1, min_len):
        for j in range(1, min_len):
            for k in range(min_len):
                for l in range(min_len):
                    if grid[i][j] == 0 and grid[k][l] == 0:
                        dp[i][j] = min(dp[i][j], dp[k][l] + 1)
                        filled[i] += 1
                        if filled[i] >= capacity_sum:
                            return filled[i]
    return filled[i]