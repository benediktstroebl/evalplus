
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

    # Get the number of wells
    n_wells = len(grid)
    # Get the width of a well
    n_columns = len(grid[0])
    # The capacity of each bucket
    bucket_capacity = capacity

    # Calculate the number of buckets
    n_buckets = math.ceil(n_wells / n_columns)

    # Get the number of units in each well
    units = [0] * n_buckets
    for well in grid:
        for index, unit in enumerate(well):
            units[index] += unit

    # Get the number of buckets we need to fill
    n_buckets_needed = 0
    for unit in units:
        if unit > 0:
            n_buckets_needed += math.ceil(unit / bucket_capacity)
    return n_buckets_needed

