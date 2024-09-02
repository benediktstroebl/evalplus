
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
    
    if capacity == 0:
        return 0

    # get the number of rows of wells
    height, _ = len(grid), len(grid[0])
    # get the total capacity for each well
    well_size = math.ceil(capacity / height)
    # register the well_flows for all wells
    well_flows = [[0 for _ in range(well_size)] for _ in range(height)]
    # register the zero_wells
    zero_wells = set()

    # fill the well_flows
    for h in range(height):
        for w in range(well_size):
            well_flows[h][w] = grid[h][(w * well_size):((w + 1) * well_size)].count(1)
        if sum(well_flows[h]) == 0:
            zero_wells.add(h)

    # fill the zero_wells
    return height - len(zero_wells)

