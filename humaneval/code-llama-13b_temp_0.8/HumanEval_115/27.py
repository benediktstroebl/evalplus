
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
    # get dimensions
    n_rows, n_columns = len(grid), len(grid[0])
    # init total number of buckets
    n_buckets = 0
    # init total number of water extracted
    n_water = 0
    # init a 'water' reference
    previous_n_water = 0
    # loop over the grid
    while previous_n_water != n_water:
        # update reference
        previous_n_water = n_water
        # init a bucket-filled well list
        filled = []
        # loop over the grid
        for row in range(n_rows):
            for column in range(n_columns):
                # check if cell is filled
                if grid[row][column] == 1:
                    # init a bucket capacity
                    capacity = 0
                    # check if cell is in filled list
                    if (row, column) in filled:
                        continue
                    # check if cell is not on the top of the grid
                    if row != 0:
                        # check if cell on top is filled
                        if grid[row-1][column] == 1:
                            # update capacity
                            capacity += 1
                            # check if cell on top is in filled list
                            if (row-1, column) in filled:
                                continue
                            # mark cell on top as filled
                            filled.append((row-1, column))
                    # check if cell is not on the bottom of the grid
                    if row != n_rows-1:
                        # check if cell on bottom is filled
                        if grid[row+1][column] == 1:
                            # update capacity
                            capacity += 1
                            # check if cell on bottom is in filled list
                            if (row+1, column) in filled:
                                continue
                            # mark cell on bottom as filled
                            filled.append((row+1, column))
                    # check if cell is not on the left of the grid
                    if column != 0:
                        # check if cell on left is filled
                        if grid[row][column-1] == 1:
