
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

    # Track the number of times we have to lower the buckets
    lower_buckets = 0

    # Track the length of each row
    row_length = len(grid[0])

    # Get the bucket capacity
    bucket_capacity = capacity

    # Track the position of the current bucket
    current_bucket = 0

    # Track the amount of water that each row can hold
    row_water = [0 for i in range(len(grid))]

    # Track the amount of water that each row has held
    row_water_filled = [0 for i in range(len(grid))]

    # Track the position of the current well
    current_well = 0

    # Track the amount of water that each well can hold
    well_water = [0 for i in range(len(grid[0]))]

    # Track the amount of water that each well has held
    well_water_filled = [0 for i in range(len(grid[0]))]

    # Fill the well_water list
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                well_water[j] += 1

    # Fill the well_water_filled list
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                well_water_filled[j] += 1

    # Calculate the total amount of water that can be extracted
    total_water = sum(well_water)

    # Calculate the maximum water that can be extracted
    maximum_water = math.ceil(total_water / bucket_capacity)

    # While we still need to lower the buckets
    while lower_buckets < maximum_water:
        # For each row
        for i in range(len(grid)):
            # For each column
            for j in range(len(grid[i])):
                # If the well has water and the bucket is empty
                if grid[i][j] == 1 and row_water[i] ==
