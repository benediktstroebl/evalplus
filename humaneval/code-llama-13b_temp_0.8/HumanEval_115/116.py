
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
    # for each well
    # fill the bucket until full
    # empty the bucket
    # move the bucket to the next well
    # if current well is empty, skip it
    # if current well is full, use it as last well
    # if current well is half full, use it as the last well
    # if last well is empty, fill it as much as possible
    # if last well is half full, do nothing
    # if last well is full, move bucket to the next row

    if not grid or not grid[0]:
        return 0
    n_wells = len(grid)
    n_wells_in_row = len(grid[0])
    wells = []
    for i in range(n_wells):
        wells += [(i, j) for j in range(n_wells_in_row) if grid[i][j] != 0]
    wells.append((n_wells, 0))
    n_wells += 1

    bucket = 0
    bucket_volume = 0
    water_poured = 0

    for well in range(len(wells)):
        if bucket_volume < capacity:
            bucket_volume = capacity
        # fill the bucket
        for b in range(bucket, wells[well][0]):
            bucket_volume -= grid[b][wells[well][1]]
            water_poured += grid[b][wells[well][1]]
            grid[b][wells[well][1]] = 0

        # empty the bucket
        for b in range(wells[well][0], bucket, -1):
            if bucket_volume == 0:
                break
            grid[b][wells[well][1]] += min(bucket_volume, capacity)
            bucket_volume -= min(bucket_volume, capacity)
            water_poured += min(bucket_volume, capacity)

        # move the bucket to the next well
        bucket = wells[well][0] + 1
        if bucket >= n_wells:
            break

    return water_poured

