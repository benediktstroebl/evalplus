
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
    
    # # Strategy
    # First, we need to understand what we are trying to achieve.
    # The solution to this problem requires the wells to be filled from top to bottom.
    # So, we need to figure out the rightmost 0 in each row.
    # If there is no 0, we can just ignore it.
    # Let's iterate through each row, find the rightmost 0, 
    # and update the maximum capacity accordingly.

    # The problem with the above strategy is that we may have a 0 in the rightmost column
    # of the last row.
    # This 0 cannot be filled by a bucket, as the bucket has a maximum capacity of 1.
    # To avoid this, we can simply go through each column and check for the rightmost 1.
    # If there is no 1, we can return 0.
    
    # Time complexity: O(mn) where m is the number of rows and n is the number of columns
    # Space complexity: O(1)

    # # Approach 1: Brute force
    # max_cols = [0] * len(grid[0])
    # for row in grid:
    #     for i in range(len(row)):
    #         if row[i] == 0:
    #             max_cols[i] = max(max_cols[i], i)
    # return sum(max_cols)

    # # Approach 2: Dynamic programming
    # # Auxiliary Space: O(n)
    # dp = [0] * len(grid[0])
    # for row in grid:
    #     max_col = 0
    #     for i in range(len(row)):
    #         if row[i] == 1:
    #             max_col = max(max_col, i)
    #         dp[i] = max(dp[i], max_col)

    # return sum(dp)

    # Approach 3: Space Optimized Dynamic Programming
    # # Auxiliary Space: O(1)
    # dp = 0
    # max_col = 0
    # for row in grid:
    #     if row[max_col] == 1:
    #         dp += 1
    #     for i in range(len(row)):
    #         if row[i] == 1:
    #            
