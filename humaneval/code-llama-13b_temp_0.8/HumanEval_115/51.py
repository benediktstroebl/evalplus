
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
    # defaultdict is not accepted
    # from collections import defaultdict
    # buckets = defaultdict(int)
    buckets = [0 for _ in range(capacity + 1)]
    row = len(grid)
    col = len(grid[0])
    print(buckets)
    for i in range(row):
        for j in range(col):
            # buckets[grid[i][j]] += 1
            # buckets[0] += 1
            buckets[grid[i][j]] += 1
    print(buckets)
    result = 0
    for bucket in buckets:
        if bucket != 0:
            print(bucket)
            result += math.ceil(bucket / capacity)
    return result
