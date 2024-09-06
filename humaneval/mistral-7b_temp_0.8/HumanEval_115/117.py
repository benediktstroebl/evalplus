
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
    m, n = len(grid), len(grid[0])
    dp = [[-1] * n for _ in range(m)]
    # Create a map of the number of blocks for each well
    blocks = [0] * m
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                blocks[i] += 1

    def find_min(well, capacity):
        """
        Find the minimum number of units that can be extracted from a well with a given capacity.
        Return the number of units that can be extracted.
        """
        if well < 0 or well >= m or capacity <= 0:
            return 0

        # If this cell has already been processed, return the previously found minimum
        if dp[well][capacity] != -1:
            return dp[well][capacity]

        # If the well is empty, it cannot be emptied, so the minimum is 0
        if blocks[well] == 0:
            dp[well][capacity] = 0
            return 0
