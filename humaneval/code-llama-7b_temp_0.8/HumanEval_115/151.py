
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
    n = len(grid)
    m = len(grid[0])
    buckets = [[0] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                buckets[i][j] = -1
                count += 1
            else:
                if i == n - 1:
                    buckets[i][j] = buckets[i][j - 1] + 1
                else:
                    buckets[i][j] = buckets[i][j - 1] + 1

    for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if buckets[i][j] == -1:
                buckets[i][j] = buckets[i + 1][j] - 1
            elif buckets[i][j] < 0:
                buckets[i][j] = buckets[i + 1][j] - 1
            else:
                buckets[i][j] = min(buckets[i + 1][j], buckets[i][j])

    for i in range(n):
        if buckets[i][0] < 0:
            return -1

    last_row = buckets[n - 1]
    bucket_count = 0
    for i in range(m):
        bucket_count += last_row[i]

    return math.ceil(bucket_count / capacity)
