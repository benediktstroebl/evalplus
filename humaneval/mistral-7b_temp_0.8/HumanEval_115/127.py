
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

    # get the length of the grid
    grid_len = len(grid)
    # get the number of buckets
    num_buckets = grid_len
    # get the maximum amount of water that can be extracted from a well
    max_extract = num_buckets * capacity
    # keep track of the number of times the bucket was lowered
    lower_bucket_count = 0
    # keep track of the amount of water extracted from a well
    water_extracted = 0

    while water_extracted < max_extract:
        # loop through all the buckets
        for bucket in range(num_buckets):
            # get the current row of the bucket
            current_row = grid[bucket]
            # loop through all the wells in the current row
            for well in range(len(current_row)):
                # check if the well has water
                if current_row[well] == 1:
                    # extract the water from the well
                    water_extracted += 1
                    # lower the bucket
                    lower_bucket_count +=
