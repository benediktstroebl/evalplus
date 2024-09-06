
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
    import numpy as np
    rows, cols = grid.shape
    bucket_capacity = capacity
    # dp[i][j] is the maximum number of water that can be put down in the well at position (i, j)
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    # top_row is the number of units of water that can be put into the well at position (0, 0)
    # dp[0][0] = grid[0][0]
    # to get the bottom row, we concatenate the grid[-1] as a row
    bottom_row = np.concatenate(grid[rows - 1])
    # to get the right-most column, we concatenate the grid[:, -1] as a column
    right_most_col = np.concatenate(grid[:, cols - 1])
    bottom_right_most = max(bottom_row, right_most_col)
    # Each bucket can put as much water as it has the capacity
    dp[rows - 1][cols - 1] = bottom_right_most
    # dp[0][1] is the maximum number of water that can be put down in the well at position (0, 1)
    # dp[1][1] is the maximum number of water that can be put down in the well at position (1, 1)
    for i in range(rows - 2, -1, -1):
        for j in range(cols - 2, -1, -1):
            water_in_the_well = grid[i][j]
            top_row = dp[i + 1][j]
            right_most_col = dp[i][j + 1]
            dp[i][j] = max(water_in_the_well + top_row, water_in_the_well + right_most_col, bottom_capacity)
    # convert dp to an array and return its maximum value
    return int(max(dp[0]))

