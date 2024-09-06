
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
    # Find the length of the wells
    wells_length = len(grid[0])

    # Track the highest level of water
    max_level = 0
    # Track the number of times the buckets are used
    used_buckets = 0

    # Iterate over each well
    for well in grid:
        # Track the total amount of water in the well
        total_water = 0

        # Iterate over each well
        for water_unit in well:
            # Keep track of the total amount of water in the well
            total_water += water_unit
        
        # Update the max_level value if needed
        if total_water > max_level:
            max_level = total_water
        
        # If the max level has exceeded the capacity, we need to empty the well
        if max_level > capacity:
            # Update the number of times the buckets are used
            used_buckets += math.ceil(max_level / capacity)
            # Reset the max level to account for the emptying
            max_level = total_water

    return used_buckets
