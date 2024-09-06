
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
    # Extract out the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # STEP 1: 
    # Initialize a bucket that holds the amount of water
    bucket = capacity

    # STEP 2:
    # Iterate over the columns (from left to right) of the grid
    # NOTE: The left-most column represents the column of the first well
    # NOTE: The right-most column represents the column of the last well
    for col in range(cols):

        # STEP 3:
        # Keep track of the number of wells that we've "emptied" (contain 0 water)
        # NOTE: we only need to keep track of this variable if we want to output
        # the number of times that we had to lower a bucket
        zero_wells = 0

        # STEP 4:
        # Iterate over the rows (from top to bottom) of the grid
        # NOTE: The top-most row represents the row of the first well
        # NOTE: The bottom-most row represents the row of the last well
        for row in range(rows):

            # STEP 5:
            # Determine if the current well has water
            well_has_water = grid[row][col]

            # STEP 6:
            # If the current well does not contain water, then we've emptied it
            if not well_has_water:
                # Increment the number of wells that we've emptied
                zero_wells += 1
                # Continue to the next well
                continue

            # STEP 7:
            # If the current well does contain water, then we need to extract it
            else:
                # Decrement the amount of water in the bucket
                bucket -= 1
                # Continue to the next well
                continue

        # STEP 8:
        # If the current bucket is empty, then the current column of wells are fully
        # drained, so we can move on to the next column of wells
        if bucket <= 0:
           
