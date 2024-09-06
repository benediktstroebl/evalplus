
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
    # Edge Cases
    if len(grid) == 0:
        return 0
    if len(grid) == 1 and len(grid[0]) == 0:
        return 0
    if capacity == 0:
        return 0
    
    # Approach
    # Find the biggest row
    # Find the biggest column

    # Will this be O(n^2)?
    # I believe it's O(n)

    # Create a buckets list
    # Create a bucket capacity variable

    # Iterate through grid
    #   If we come across a well
    #       If the well is greater than capacity
    #           Add the well to the buckets
    #       Else
    #           Add the well to the buckets and continue
    
    # If the buckets is greater than 0
    #   Subtract the bucket capacity from the buckets
    #   Return the buckets
    # Else
    #   return 0

    # Create a buckets list
    buckets = []

    # Create a bucket capacity variable
    bucket_capacity = capacity

    # Iterate through grid
    for well in grid:
        # If the well is greater than capacity
        if well > bucket_capacity:
            # Add the well to the buckets
            buckets += well
        # Else
        else:
            # Add the well to the buckets and continue
            buckets += well
            continue

    # If the buckets is greater than 0
    if len(buckets) > 0:
        # Subtract the bucket capacity from the buckets
        buckets -= bucket_capacity
        # Return the buckets
        return len(buckets)
    # Else
    else:
        # return 0
        return 0
