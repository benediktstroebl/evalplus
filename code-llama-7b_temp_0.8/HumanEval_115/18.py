
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
    # Return 0 if no wells exist
    if not grid:
        return 0
    # Return 0 if grid is empty
    if not grid[0]:
        return 0

    # Initialize variables
    wells = grid
    bucket_capacity = capacity

    # Initialize variables for helper methods
    bucket_level = 0
    current_bucket_capacity = 0
    num_times_lowered = 0

    # Methods
    def move_water_from_well_to_bucket(well_idx):
        nonlocal current_bucket_capacity
        nonlocal bucket_capacity
        nonlocal num_times_lowered
        nonlocal bucket_level

        # Move water to current bucket
        if wells[well_idx][bucket_level] > 0:
            if current_bucket_capacity < bucket_capacity:
                wells[well_idx][bucket_level] -= 1
                current_bucket_capacity += 1
            else:
                wells[well_idx][bucket_level] -= 1
                current_bucket_capacity += 1
                num_times_lowered += 1

        return num_times_lowered

    def move_water_from_bucket_to_well(well_idx):
        nonlocal current_bucket_capacity
        nonlocal bucket_capacity
        nonlocal num_times_lowered
        nonlocal bucket_level

        # Move water from current bucket to well
        if wells[well_idx][bucket_level] == 0:
            if current_bucket_capacity > 0:
                wells[well_idx][bucket_level] += 1
                current_bucket_capacity -= 1
                num_times_lowered += 1

        return num_times_lowered

    # Main algorithm
    while current_bucket_capacity > 0:
        # Move water from wells to buckets
        for well_idx in range(0, len(wells)):
            num_times_lowered = move_water_from_well_to_bucket(well_idx)

        # Move water from buckets to wells
