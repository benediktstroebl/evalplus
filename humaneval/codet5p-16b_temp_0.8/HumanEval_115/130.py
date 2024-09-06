
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

    
    def get_bucket_capacity(row):
        num_ones = 0
        bucket_capacity = 0
        for i, e in enumerate(row):
            if e == 1:
                num_ones += 1
                bucket_capacity = max(bucket_capacity, i+1)
        return num_ones, bucket_capacity


    rows, cols = len(grid), len(grid[0])
    num_buckets = rows * cols

    bucket_capacity = math.inf
    num_empties = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                num_empties += 1
            else:
                num_ones, bucket_capacity = get_bucket_capacity(grid[i])
                if bucket_capacity > capacity:
                    num_empties += bucket_capacity - capacity

    return num_empties

