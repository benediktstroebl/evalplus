
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
    # get the height of the grid
    rows = len(grid)
    cols = len(grid[0])

    # make a copy of the grid
    grid_copy = [i[:] for i in grid]

    # get the maximum number of full wells
    num_full_wells = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                num_full_wells += 1
    max_full_wells = num_full_wells

    # fill up the grid, note this can be done in-place because
    # we are not actually storing any additional information
    count = 0
    while num_full_wells > 0:
        count += 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for x in range(i, rows):
                        if grid_copy[x][j] == 0:
                            grid[i][j] = 0
                            grid_copy[x][j] = 1
                            num_full_wells -= 1
                            break
                        elif x == rows - 1:
                            # if we are here, it means there is
                            # no room for the well
                            max_full_wells -= 1
                            grid[i][j] = 0
                            num_full_wells -= 1
                        else:
                            # we cannot take the well
                            pass
    return count if max_full_wells == 0 else math.inf

