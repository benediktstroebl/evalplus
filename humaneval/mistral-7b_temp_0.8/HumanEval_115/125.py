
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

    # Initialize solution counter
    solution_count = 0
    # Initialize max_water_count
    max_water_count = 0
    # Initialize wells_list
    wells_list = []
    # Initialize wells_list_index
    wells_list_index = 0
    # Iterate over grid
    for i in range(len(grid)):
        # Initialize well_water_count
        well_water_count = 0
        # Iterate over grid[i]
        for j in range(len(grid[i])):
            # If grid[i][j] == 1
            if grid[i][j] == 1:
                # Increment well_water_count
                well_water_count += 1
                # Add well_water_count to wells_list
                wells_list.append(well_water_count)
                # Increment wells_list_index
                wells_list_index += 1
            # Else
            else:
                # Add 0 to wells_list
