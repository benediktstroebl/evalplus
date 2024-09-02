
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
    from collections import deque
    count = 0
    def fill_bucket(q, capacity):
        while q:
            if q[0].capacity <= capacity:
                q[0].capacity += q[0].bucket.pop()
            else:
                break
            count += 1
            
    buckets = [[Queue(capacity) for j in range(len(grid[0]))] for i in range(len(grid))]
    for row in grid:
        for i, v in enumerate(row):
            if v > 0:
                buckets[i][v-1].bucket.append(1)
    
    for bucket in buckets:
        fill_bucket(bucket, capacity)
    
    return
