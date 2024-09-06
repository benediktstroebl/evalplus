
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
    # get the number of wells
    n_wells = len(grid)
    # get the number of rows
    n_rows = len(grid[0])
    # get the number of buckets
    n_buckets = capcity 
    # initialize the the buckets if all wells are full
    init_buckets = [True] * n_buckets
    # initialize the buckets for all wells
    buckets = [[init_buckets[:] for i in range(n_rows)] for j in range(n_wells)]
    # loop for all wells
    for well_idx in range(n_wells):
        for row_idx in range(n_rows):
            # set the correct bucket for each grid
            if grid[well_idx][row_idx] == 0:
                buckets[well_idx][row_idx] = False
            else:
                buckets[well_idx][row_idx] = [False] * n_buckets
    # loop for every bucket
    for bucket_idx in range(n_buckets):
        flag = 1 # initialize the flag
        # loop for all wells
        for well_idx in range(n_wells):
            # loop for all rows
            for row_idx in range(n_rows):
                # let the row fill within the bucket
                if buckets[well_idx][row_idx][bucket_idx]:
                    buckets[well_idx][row_idx][bucket_idx] = False
                    buckets[well_idx][row_idx][bucket_idx] = True
                    # check if the bucket is all filled
                    if sum(sum(buckets[well_idx][row_idx], [])) == n_buckets:
                        flag = 0
                        break
            if flag == 0:
                break
        # check if all buckets are filled
        if flag == 1:
            return bucket_idx
            break
    # if not all wells are empty
    return n_buckets
