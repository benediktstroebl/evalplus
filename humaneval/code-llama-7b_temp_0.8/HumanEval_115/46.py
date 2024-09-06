
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
    #<--
    # the number of rows in grid
    row_count = len(grid)
    # the number of columns in grid
    column_count = len(grid[0])
    # initialize buckets with capacity
    buckets = capacity
    # initialize a counter to represent the number of times buckets must be lowered
    count = 0
    # initialize a counter to represent the number of times a bucket has been filled
    filled_buckets = 0
    # while there are still buckets to be filled
    while filled_buckets < row_count * column_count:
        # for each column in grid
        for column in range(0, column_count):
            # if there is water at the current column
            if grid[column] != 0:
                # lower a bucket into the well at the current column
                buckets -= grid[column]
                # if the bucket is empty
                if buckets == 0:
                    # increase the count
                    count += 1
                    # increase the number of filled buckets
                    filled_buckets += column_count
                    # reset the capacity
                    buckets = capacity
        # for each row in grid
        for row in range(0, row_count):
            # if there is water at the current row
            if grid[row] != 0:
                # lower a bucket into the well at the current row
                buckets -= grid[row]
                # if the bucket is empty
                if buckets == 0:
                    # increase the count
                    count += 1
                    # increase the number of filled buckets
                    filled_buckets += row_count
                    # reset the capacity
                    buckets = capacity
        # if there is still water in the wells
        if filled_buckets < row_count * column_count:
            # for each row in grid
            for row in range(0, row_count):
                # for each column in grid
                for column in range(0, column_count):
                    # if there is water at the current row and column
                    if grid[row][column] != 0:
                        # increase the capacity of the current well
                       
