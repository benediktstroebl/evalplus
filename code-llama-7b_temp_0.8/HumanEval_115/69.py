
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
    # the index of the wells
    wells = [i for i in range(len(grid)) if 1 in grid[i]]
    # the index of the wells
    buckets = [0] * len(grid)
    # calculate the number of wells filled
    filled_wells = sum(grid[i].count(1) for i in range(len(grid)))
    # calculate the number of buckets needed
    count_buckets = math.ceil(filled_wells / capacity)
    # the number of times that lower the bucket
    count_lift = 0
    # while there is not enough water
    while filled_wells < capacity * count_buckets:
        # iterate over each well
        for i in wells:
            # if there is water in the well
            if grid[i].count(1) != 0:
                # empty the well
                grid[i] = [0] * len(grid[i])
                # increment the counter of the bucket
                buckets[i] += 1
                # if there is enough water
                if buckets[i] == capacity:
                    # increment the counter of the buckets
                    count_buckets += 1
                    # remove the well
                    wells.remove(i)
        # if there is enough water
        if count_buckets > 1:
            # increment the counter of the buckets
            count_buckets -= 1
            # increment the counter of the buckets
            count_lift += 1
    # return the number of times that lower the bucket
    return count_lift
