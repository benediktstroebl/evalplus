
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
    #print(grid, capacity)
    import math
    grid = grid[::-1]
    max_well_len = len(grid)
    max_well_capacity = len(grid[0])
    current_bucket = 0
    current_well = 0
    total_buckets = 0

    while current_well < max_well_len:
        total_water = 0
        while current_well < max_well_len and grid[current_well][current_bucket] == 0:
            current_well += 1

        current_well = max(current_well, 0)

        #print("HERE" * 20, grid[current_well], current_bucket, current_well)

        while current_well < max_well_len and grid[current_well][current_bucket] == 1:
            #print("HOI", grid[current_well], current_well, current_bucket)
            total_water += grid[current_well][current_bucket]
            grid[current_well][current_bucket] = 0
            current_well += 1

        if total_water == 0:
            return -1

        if total_water <= capacity:
            capacity -= total_water
            total_buckets += 1
        else:
            total_buckets += math.ceil(total_water / capacity)

        capacity = capacity % capacity
        #print(total_water, capacity, total_buckets)
        current_bucket += 1
        if current_bucket >= max_well_capacity:
            current_bucket = 0
            current_well += 1

    return total_buckets

