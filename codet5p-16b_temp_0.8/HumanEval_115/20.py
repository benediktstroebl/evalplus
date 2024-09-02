
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

    h = len(grid)
    w = len(grid[0])
    dp = [[math.inf for _ in range(capacity+1)] for _ in range(h)]

    def water(j,i,c):
        if dp[i][c] == math.inf:
            dp[i][c] = 0
        if j == w-1:
            return 0
        return (grid[i][j+1] - grid[i][j] - 1) + water(j+1,i,c)
    
    dp[0][0] = water(0,0,0)
    
    for i in range(h):
        for c in range(1,capacity+1):
            if c < capacity:
                dp[i][c] = min(dp[i][c],dp[i][c-1]+water(0,i,c-1))
            if c >= 1:
                dp[i][c] = min(dp[i][c],dp[i][c-1]+water(w-1,i,c-1))
    
    
