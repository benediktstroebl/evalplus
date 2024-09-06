
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

    if not grid or not grid[0]:
        return 0

    height, width = len(grid), len(grid[0])
    wells = height * width

    # create a map for the buckets
    map = {}

    # go through every well, and if it has water in it, put a bucket in the map with the bucket's position (in the list)
    # and the water volume (in that position)
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                map[height * i + j] = 1

    # sort the buckets map
    map = dict(sorted(map.items(), key=lambda x: x[1]))

    # total buckets count
    buckets = len(map)

    # if there are more buckets than wells, it can't be solved
    if buckets > wells:
        return -1

    # fill the buckets
    while True:

        # list of the buckets positions that are going to be filled in this iteration
        filled = []

        # list of the buckets positions that have been filled and need to be refilled
        full = []

        # iterate through the buckets and fill them as much as they can
        for bucket, volume in map.items():

            # the bucket has been filled enough
            if volume == capacity:
                continue

            # find all adjacent buckets to the current one
            adj = find_adj(map, bucket, width, height)

            # iterate through the adjacent buckets, and fill them if they can
            for other in adj:

                # the bucket is currently empty
                if map[other] == 0:
                    continue

                # if the bucket's volume + the adjacent bucket's volume < the bucket's capacity, fill it
                if map[other] + map[bucket] <= capacity:
                    map[other] = 0
                    map[bucket] += map[other]
                    filled.append(other)

                # if the bucket's volume + the adjacent bucket's volume > the bucket's capacity, 
