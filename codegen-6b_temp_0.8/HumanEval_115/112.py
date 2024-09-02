
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
    # keep track of wells that have not been filled
    # bucket_num, wells_used, needed_fill
    wells_used = 0
    wells_left = [j for j in range(len(grid[0]))]

    while wells_used < len(grid[0]) - 1:
        # find the well with the max fill
        possible_wells = []
        for well_index in wells_left:
            well = grid[well_index]
            max_fill_well = well.index(max(well))
            possible_wells.append(max_fill_well)

        # find the well with the min fill
        min_fill_well = possible_wells[0]
        for i in range(1, len(possible_wells)):
            if possible_wells[i] < min_fill_well:
                min_fill_well = possible_wells[i]

        well_index = min_fill_well
        well = grid[well_index]
        wells_left.remove(well_index)

        # fill the well
        wells_used += 1
        capacity_used = 0
        while capacity_used < capacity:
            capacity_used += 1
            for i in range(len(well)):
                well[i] -= 1
        
    return wells_used

