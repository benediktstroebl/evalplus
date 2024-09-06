
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
    # Calculate the width of the grid
    width = len(grid[0])
    height = len(grid)

    # Initialize the number of times the buckets are lowered
    num_lowered = 0
    water_in_wells = 0

    # Iterate over the grid
    for i in range(height):
        for j in range(width):
            # If the grid cell contains water, add it to the water_in_wells
            if grid[i][j] == 1:
                water_in_wells += 1

            # If the bucket capacity is less than or equal to the remaining water in the wells
            # lower the bucket
            if capacity <= water_in_wells:
                num_lowered += 1
                # Update the water_in_wells
                water_in_wells -= capacity

    return num_lowered
