
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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    import queue

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # bucket capacity
    capacity = bucket_capacity

    # wells rows
    wells = grid

    # minimum height of well
    min_height = min([len(well) for well in wells])

    # maximum height of well
    max_height = max([len(well) for well in wells])

    # wells column count
    wells_len = len(wells)

    # wells rows count
    wells_rows = len(wells[0])

    # bucket initial level
    bucket_level = 0

    # moves count
    moves = 0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # order wells by column
    order = [(wells[column][row], column, row) for row in range(wells_rows) for column in range(wells_len)]

    # sort order
    order = sorted(order, key=lambda well: well[0], reverse=True)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # loop until all wells are empty or bucket is full
    while order and bucket_level < capacity:

        # pop the highest well
        high_well, high_column, high_row = order.pop()

        # well is full
        if not high_well:

            # move to
