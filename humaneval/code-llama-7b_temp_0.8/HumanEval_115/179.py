
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
    buckets = []
    for row in grid:
        for element in row:
            if element == 1:
                buckets.append(1)
    buckets_num = len(buckets)
    buckets_capacity = capacity

    if buckets_num == 0:
        return 0

    print("buckets length: {}".format(len(buckets)))
    print("buckets capacity: {}".format(capacity))

    counter = 0
    while True:
        print("count {} buckets".format(buckets_num))
        for i in range(buckets_num):
            if buckets[i] == buckets_capacity:
                buckets[i] = 0
                counter += 1
        print("{} buckets left".format(buckets_num))
        if buckets_num == 0:
            return counter
        for i in range(buckets_num - 1, 0, -1):
            if buckets[i] != 0:
                buckets[i] += buckets[i - 1]
                buckets[i - 1] = 0
                counter += 1
        buckets_num -= 1
















