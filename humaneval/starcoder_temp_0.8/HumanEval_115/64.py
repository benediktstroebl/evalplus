
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
    # the max amount of water that can be in a row
    max_capacity = len(grid) * capacity
    # for every row:
    #   * how much water can be added to the current row
    #   * how much water can be removed from the previous row
    #   * how much water can be removed from the current row
    #   * how much water can be removed from the next row
    dp = [[(0,0,0,0) for i in range(len(grid[0]) + 1)] for j in range(len(grid) + 1)]
    # we have to fill the last row first, so the wells are bottom up
    for j in range(len(grid[0]) - 1, -1, -1):
        for i in range(len(grid) - 1, -1, -1):
            cap = capacity
            prev = dp[i+1][j+1]
            # if the well is open:
            if grid[i][j] == 0:
                cap -= 1
            next_ = dp[i][j+1]
            # if the next well is open:
            if grid[i+1][j] == 0:
                cap -= 1
            # if we have to fill a new well, 
            # the max amount of water that can go down is the capacity of the bucket
            if cap == 0:
                # how much water we add in this row
                dp[i][j] = (prev[0] + cap, prev[1] + cap, 0, 0)
            else:
                # how much water we add in this row
                # is the previous max amount of water added to the previous row
                # or the previous max amount of water removed from the next row
                dp[i][j] = (max(prev[0], next_[1]) + cap,
                            max(prev[1], next_[0]),
                            prev[2] + next_[3],
                            prev[3] + next_[2])
            # if we have to empty a well,
            # the max amount of water that can go down is the previous max amount of water
            # added to the previous row
            if grid[i][j] == 1:
                dp[i][j] = (dp[i][j][0], dp[i][j][1], prev[0
