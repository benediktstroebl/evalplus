
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
    # Create an empty list to store the number of times the bucket is lowered
    num_of_times_lowered = [0] * len(grid)
    
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each column in the row
        for j in range(1, len(grid[i])+1):
            # If the cell is not empty (meaning it already has water), 
            # and if it has water and the water is less than the capacity of the bucket, 
            # then lower the bucket from the well
            if grid[i][j-1] == 1 and grid[i][j-1] <= grid[i][j]:
                num_of_times_lowered[i][j] = num_of_times_lowered[i][j] + 1
    
    # Return the maximum number of times the bucket is lowered
    return max(num_of_times_lowered)
