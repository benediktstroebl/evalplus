
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
    # Waiting to solve this one
    height, width = len(grid), len(grid[0])
    if height <= 0 or width <= 0:
        return 0

    # Compute the maximum number of times a bucket can be dropped
    # to empty the grid
    max_bucket_drops = (height * width) / capacity

    # Initialize the total amount of water
    # and the number of bucket drops
    total_water = 0
    bucket_drops = 0

    # Start by dropping the bucket from the top left corner
    # and move left to right
    for i in range(width):
        # Add the amount of water in the current column
        total_water += grid[0][i]

        # Check if the bucket is full or if the total
        # amount of water is greater than the bucket capacity
        if (total_water > capacity) or (i == width - 1):
            # Drop the bucket, add the number of drops
            # and reset the total amount of water
            total_water = 0
            bucket_drops += 1
            # Check if there are still bucket drops remaining
            if bucket_drops == max_bucket_drops:
                return bucket_drops

    # Reset the number of bucket drops
    bucket_drops = 0

    # Start by dropping the bucket from the bottom right corner
    # and move left to right
    for i in range(width - 1, -1, -1):
        # Add the amount of water in the current column
        total_water += grid[height - 1][i]

        # Check if the bucket is full or if the total
        # amount of water is greater than the bucket capacity
        if (total_water > capacity) or (i == 0):
            # Drop the bucket, add the number of drops
            # and reset the total amount of water
            total_water = 0
            bucket_drops += 1
            # Check if there are still bucket drops remaining
            if bucket_drops == max_bucket_drops:
                return bucket_drops

    # Start by dropping the bucket from the top
