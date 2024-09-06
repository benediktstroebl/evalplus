
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
    # Your Code
    row = len(grid)
    col = len(grid[0])

    # dp[i][j] = 
    #     | the minimum number of buckets required to empty the water at cell (i,j)
    #     | if we have not been there before
    #     | the minimum number of buckets required to empty the water at cell (i,j)
    #     | if we have been there before
    dp = [[0 for _ in range(col)] for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                # if we have not been there before
                if dp[r][c] == 0:
                    dp[r][c] = math.inf
                # if we have been there before
                if dp[r][c] > 0:
                    dp[r][c] = math.inf

    # the following is the main idea of the solution
    # we use dp[i][j] to store the
