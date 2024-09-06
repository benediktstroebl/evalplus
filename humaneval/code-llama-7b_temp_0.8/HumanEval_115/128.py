
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

    # Is there a more efficient way to do this?

    height, width = len(grid), len(grid[0])
    buckets = [bucket_capacity] * len(grid)
    water_at_well = 0
    for row in grid:
        for well in row:
            if well == 1:
                water_at_well += 1

    times_to_empty_wells = math.ceil(water_at_well / bucket_capacity)
    if times_to_empty_wells == 0:
        return 0

    # We only need to subtract one, since our initial
    # water_at_well is already included in the calculation
    times_to_empty_wells -= 1

    # The number of times we need to lower the buckets
    total_times_to_empty = 0

    # Keep going until all wells are empty
    while water_at_well > 0:
        # How much water can we add at once?
        total_times_to_empty += 1
        # Subtract one from each bucket
        buckets = [b - 1 for b in buckets]
        # Keep track of how much water we have left
        water_left = 0
        # How many buckets are empty?
        empty_buckets = 0
        for i in range(len(buckets)):
            # Keep track of how much water is in the buckets
            water_left += buckets[i]
            # How many buckets are empty?
            if buckets[i] == 0:
                empty_buckets += 1

        # How much water do we need to fill in?
        water_needed = water_at_well - water_left
        # How many times do we need to fill?
        times_to_fill = math.ceil(water_needed / empty_buckets)
        # Keep track of the water left over
        water_left_over = water_needed % empty_buckets
        # How many times do we need to fill the wells?
        for i in range(times_to_fill):
            # How much water is left over
