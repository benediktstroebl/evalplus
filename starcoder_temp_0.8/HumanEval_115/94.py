
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
    # Initialize variables
    height = len(grid)
    width = len(grid[0])
    # Initialize output
    num_buckets_used = 0
    # Initialize buckets
    buckets = []
    # Compute the maximum amount of water that can be contained in each cell
    for row in range(height):
        for col in range(width):
            buckets.append(min(grid[row][col], capacity))
    # Loop through every cell in the grid
    for row in range(height):
        for col in range(width):
            # Compute the number of empty buckets that can be used to fill up this cell
            num_buckets_used += math.ceil(buckets[row*width + col] / capacity)
            # Update the number of empty buckets in the cell itself
            buckets[row*width + col] = min(buckets[row*width + col], capacity - grid[row][col])
    # Return the number of empty buckets
    return num_buckets_used
