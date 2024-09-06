
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
    # Sum up the number of wells
    # Sum up the number of filled wells
    # Sum up the number of empty wells
    # How many times do you need to lower the buckets?
    # At least once if all wells are empty
    # If all wells are empty, how many times do you need to lower the buckets?
    # If all wells are filled, how many times do you need to lower the buckets?
    # If the wells are half-full, how many times do you need to lower the buckets?
    # If the wells are three-quarters-full, how many times do you need to lower the buckets?
    # If the wells are full, how many times do you need to lower the buckets?
    # Create a grid of buckets
    # Loop through each well
        # If the well is empty
            # Fill the bucket
            # Lower the bucket
        # Else if the well is full
            # Empty the bucket
            # Lower the bucket
        # Else if the well is half-full
            # Empty the bucket
            # Lower the bucket
    # Return the number of times you need to lower the buckets

    import math

    # Create a grid of buckets
    n = len(grid)
    m = len(grid[0])
    bucket_grid = [[None] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                bucket_grid[i][j] = Bucket(0)
            else:
                bucket_grid[i][j] = Bucket(1)

    # Loop through each well
    # If the well is empty
    # Fill the bucket
    # Lower the bucket
    # If the well is full
    # Empty the bucket
    # Lower the bucket
    # If the well is half-full
    # Empty the bucket
    # Lower the bucket
    count = 0
    for i in range(n):
        for j in range(m):
            bucket = bucket_grid[i][j]
            well = grid[i][j]
            if
