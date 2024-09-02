
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
    wells, well_count = grid, len(grid[0])
    # 1. determine the top-down path to achieve the goal
    # 2. determine the bottom-up path to achieve the goal
    # 3. number of times we need to lower buckets = len(top-down path) - len(bottom-up path)

    def top_down():
        # solve top-down using dynamic programming
        # need to find the maximum number of buckets to fill up the wells
        # can we start at the first row, and traverse to the end?
        # yes, we can, in that case, we need to sum up all the wells from the first row
        # alternatively, we can start from the last row, and traverse back to the first row
        # initialize the dp array to have the value of the first well
        # and the rest of the row to be 0
        # then, compute all the rows and find the maximum number of buckets
        # we can fill up
        for row in range(well_count-1, -1, -1):
            for col in range(well_count):
                if row == well_count-1:
                    dp[row][col] = wells[row][col]
                else:
                    dp[row][col] = max(dp[row+1][col], wells[row][col])
        return dp

    def bottom_up():
        # need to find the minimum number of buckets to fill up the wells
        # can we start at the first row, and traverse to the end?
        # yes, we can, in that case, we need to sum up all the wells from the first row
        # alternatively, we can start from the last row, and traverse back to the first row
        # initialize the dp array to have the value of the first well
        # and the rest of the row to be 0
        # then, compute all the rows and find the minimum number of buckets
        # we can fill up
        for row in range(well_count):
            for col in range(well_count):
                if row == 0:
                    dp[row][col] = wells
