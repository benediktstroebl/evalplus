
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
    bucket_volume = 0
    nb_operations = 0
    # for each well
    for i in range(len(grid)):
        j = 0
        # for each bucket
        while j < len(grid[i]) and bucket_volume < capacity:
            # if the bucket is not full
            if bucket_volume < capacity:
                # if the well has water
                if grid[i][j] == 1:
                    # fill the bucket
                    bucket_volume += 1
                # if the well has no water, just skip
                else:
                    j += 1
            # if the bucket is full
            else:
                nb_operations += 1
                # if the well has water
                if grid[i][j] == 1:
                    # empty the bucket
                    bucket_volume = 0
                # if the well has no water, just skip
                else:
                    j += 1
    # empty the last bucket
    nb_operations += math.ceil(bucket_volume / capacity)
    return nb_operations

