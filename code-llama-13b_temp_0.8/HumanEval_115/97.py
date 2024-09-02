
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
    # limit = 0
    # for row in grid:
    #     limit += row.count(1)
    # print(limit)
    limit = sum([row.count(1) for row in grid])
    print(limit)
    if limit <= capacity:
        return 0
    elif capacity == 1:
        return limit
    elif capacity >= 2:
        h = len(grid)
        l = len(grid[0])
        i = 0
        j = 0
        bucket = 0
        bucket_capacity = capacity
        water = 0
        count = 0
        if i == h-1 and j == l-1:
            return 0
        while True:
            if bucket == 0:
                count += 1
            # if (i == 0 or grid[i-1][j] == 1) and (j < l-1 and grid[i][j+1] == 1):
            #     print("IN 1")
            #     j += 1
            #     bucket += 1
            #     water += 1
            #     if bucket_capacity == water:
            #         print(count, bucket_capacity, water)
            #         break
            #     continue
            # elif j == l-1:
            #     print("IN 2")
            #     i += 1
            #     if i == h-1:
            #         return count
            #     continue
            # else:
            #     print("IN 3")
            #     j += 1
            #     bucket += 1
            #     water += 1
            #     if bucket_capacity == water:
            #         print(count, bucket_capacity, water)
            #         break
            #     continue
            if grid[i][j] == 0:
                bucket -= 1
            else:
                bucket += 1
                water += 1
            if bucket_capacity == water:
                print(count, bucket_capacity, water)
                break
            if bucket > bucket_capacity:
                # bucket_capacity = int(math.ceil((bucket_capacity +
