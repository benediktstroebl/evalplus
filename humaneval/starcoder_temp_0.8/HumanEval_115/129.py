
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
    # This problem can be solved with dynamic programming
    # The problem is to find the number of times that water is used to fill all the wells
    # The answer is the sum of the minimums of each row 
    # -> the minimum number of times that water is used to fill all the wells at that row
    # The minimum number of times that water is used to fill the well at row i
    # is equal to the number of consecutive 1's in the row.
    # This can be solved with a dp array where dp[i] contains the minimum number of
    # times that water is used to fill the well at row i.
    # To fill the well at row i, we can take water from the well at row i - 1.
    # This can be done only if the bucket is not full.
    # If the bucket is full, we can extract the water from the well at row i - 1, 
    # only if the last unit of water that we extracted from the well at row i - 1 
    # was at the end of the bucket.
    # Otherwise, we can't fill the well at row i.
    # We can also fill the well at row i by taking water from the well at row i + 1.
    # This can be done only if the bucket is not full.
    # If the bucket is full, we can extract the water from the well at row i + 1, 
    # only if the first unit of water that we extracted from the well at row i + 1 
    # was at the beginning of the bucket.
    # Otherwise, we can't fill the well at row i.
    # Therefore, the minimum number of times that water is used to fill the well at row i 
    # is equal to the minimum of the following two cases: 
    # - the minimum number of times that water is used to fill the well at row i - 1 
    # (if the bucket is not full and if we can take water from the well at row i - 1)
    # - the minimum number of times that water is used to fill the well at row i + 1 
    # (if the bucket is not full and if we can take water from the well at row i + 1)
    # - 1 (if the bucket is full)

    # dp[i] will contain the minimum number of times that water is used to fill the well at row i.
   
