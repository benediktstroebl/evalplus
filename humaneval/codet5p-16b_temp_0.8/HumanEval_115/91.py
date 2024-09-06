
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
    dp = [[0 for i in range(cols)] for j in range(rows)]

    for j in range(cols):
        for i in range(rows):
            dp[i][j] = grid[i][j]
            if grid[i][j] == 1:
                capacity -= 1
                if capacity < 0:
                    return math.inf
            else:
                capacity = grid[i][j]
    
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if dp[i][j] == 1:
                dp[i][j] = min(dp[i][j + 1], dp[i + 1][j])
            if dp[i][j] == 0:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])

    return int(sum(sum(row) for row in dp))

