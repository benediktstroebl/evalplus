
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
    # get size of grid
    grid_size = len(grid)
    # get number of wells
    num_wells = len(grid[0])
    # create list to store number of wells per row
    wells_per_row = []
    # loop through each row
    for row_idx, row in enumerate(grid):
        # store the number of wells in the current row
        wells_per_row.append(sum(row))
        # determine how many times to empty buckets in the current row
        num_times_buckets_empty = math.ceil(wells_per_row[row_idx]/capacity)
        # loop through each well in the current row
        for well_idx, well in enumerate(row):
            # if the well is full
            if well == 1:
                # determine how many times to empty the buckets
                num_times_buckets_empty = math.ceil(num_wells/capacity)
                # loop through the number of times to empty the buckets
                for empty_bucket_idx in range(num_times_buckets_empty):
                    # if it is the last bucket
                    if empty_bucket_idx == num_times_buckets_empty-1:
                        # if the well is in the last bucket
                        if well_idx == (num_wells - (num_times_buckets_empty*capacity)):
                            # do not change the well
                            continue
                    # increment the index to the next well
                    well_idx = well_idx + capacity
                    # if the well is full
                    if grid[row_idx][well_idx] == 1:
                        # change the well to empty
                        grid[row_idx][well_idx] = 0
                    # else
                    else:
                        # break out of the loop
                        break
    # return the sum of the wells per row
    return sum(wells_per_row)

