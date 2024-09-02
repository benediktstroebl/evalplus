
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
    # ASSUMPTION: Each row is a well, and each column is a bucket
    #             All wells are filled with water
    #             Each bucket has a constant capacity
    #             Water is collected from the wells using the buckets
    #             Each column represents a bucket
    #             Each row represents a well
    #             We are given a grid which is a matrix of ones and zeros
    #             Grid[row][col] = 1 is considered water at well[row]
    #             Grid[row][col] = 0 is considered empty space
    #             Water is collected by the buckets using the following algorithm
    #                   Buckets fill up with water until full
    #                   Buckets are then lowered to the next well
    #                   This is done until all wells are empty
    #
    #             Input grid is a matrix of 1's and 0's
    #             Output: Number of times buckets need to be lowered
    #
    # TIME COMPLEXITY: O(row*col)
    # SPACE COMPLEXITY: O(1)
    #
    # @param grid, a 2D matrix of 0's and 1's
    # @param bucket_capacity, an int representing capacity of bucket
    # @returns an int representing number of times the buckets were lowered
    def max_fill(grid, bucket_capacity):
        if not grid or not bucket_capacity:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        buckets = bucket_capacity

        num_times_lowered = 0
        row = 0
        col = 0

        # Iterate over each row
        while row < rows:
            # Iterate over each column
            while col < cols:
                # If there is a water unit, then add to the bucket
                if grid[row][col] == 1:
                    buckets += 1
                    # If the bucket is full, then move to the next well
                    if buckets == bucket_capacity:
                        num_times_lowered += 1
                        bu
