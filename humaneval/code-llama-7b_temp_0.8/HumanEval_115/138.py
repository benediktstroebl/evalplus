
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
    # Initialization
    bucket_capacity = capacity
    grid_length = len(grid)
    wells = []

    # Setting up wells
    for i in range(grid_length):
        wells.append([])
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                wells[i].append(j)

    # Checking if the problem can be solved
    if len(wells) == 0:
        return 0
    
    # Sorting wells based on length of well
    sorted_wells = []
    for well in wells:
        if len(well) != 0:
            sorted_wells.append([len(well), well])

    sorted_wells = sorted(sorted_wells, key=lambda x: x[0], reverse=True)

    # Solving problem
    current_bucket_capacity = 0
    current_well_idx = 0
    current_well_bucket_idx = 0
    bucket_count = 0
    while current_bucket_capacity < bucket_capacity:
        # Choose the next well
        if current_well_idx >= len(sorted_wells):
            break
        current_well_capacity = len(sorted_wells[current_well_idx][1])
        current_well_idx += 1

        # Choose the next bucket
        current_well_bucket_capacity = sorted_wells[current_well_idx - 1][0]
        current_well_bucket_idx = 0
        while current_well_bucket_capacity > 0 and current_well_bucket_idx < current_well_capacity:
            current_well_bucket_capacity -= 1
            current_well_bucket_idx += 1

        # Filling the bucket
        current_bucket_capacity += 1
        bucket_count += 1

    return bucket_count
