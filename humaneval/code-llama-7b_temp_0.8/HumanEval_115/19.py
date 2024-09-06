
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

    n_rows = len(grid)
    n_cols = len(grid[0])
    n_buckets = n_rows * n_cols

    # Initialize empty bucket array, where each index represents the bucket at that position
    buckets = [0] * n_buckets

    # Calculate bucket capacity of each bucket
    bucket_capacity = capacity // (n_rows + 1)

    # Total number of bucket used
    used = 0

    # Total number of buckets needed
    needed = 0

    # Get the total number of water in each well
    for row in grid:
        used += row.count(1)

    # Check if it is possible to empty the wells
    if used > bucket_capacity * n_buckets:
        return math.inf

    # Check if we have empty wells
    if used == 0:
        return 0

    # Calculate the number of buckets needed
    needed = used // bucket_capacity

    # Count the number of times we need to lower the buckets
    count = 0

    for i in range(n_rows):
        for j in range(n_cols):
            # If there is water in the well
            if grid[i][j] == 1:
                # Set the corresponding bucket to have the bucket capacity
                buckets[i * n_cols + j] = bucket_capacity
                needed -= 1

    # Lower the buckets if we can empty the wells
    while needed > 0:
        # Count number of times we have lowered the buckets
        count += 1

        # Reset the number of times we need to lower the buckets
        needed = 0

        # Iterate over all the wells
        for i in range(n_rows):
            for j in range(n_cols):
                # If we need to empty the well and we can lower the bucket
                if grid[i][j] == 1 and buckets[i * n_cols + j] > 0:
                    buckets[i * n_cols + j] -= 1
                    needed -= 1
                    #
