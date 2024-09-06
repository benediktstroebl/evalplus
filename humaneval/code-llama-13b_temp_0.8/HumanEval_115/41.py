
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
    m = len(grid)
    n = len(grid[0])
    row_cnt = 0

    # count wells that can be drained in 1 pass
    for i in range(m):
        row_cnt += math.ceil(grid[i].count(1) / capacity)

    # count wells that can be drained in 2 passes
    cnt = 0
    for i in range(m):
        for j in range(n):
            # current bucket
            cnt = math.ceil(grid[i][j] / capacity)
            if cnt == 1:
                continue
            
            # left bucket
            left = 0
            if j-1 >= 0 and grid[i][j-1] > 0:
                left = math.ceil(grid[i][j-1] / capacity)
            
            # right bucket
            right = 0
            if j+1 < n and grid[i][j+1] > 0:
                right = math.ceil(grid[i][j+1] / capacity)

            # count wells that can be drained in 2 passes
            if left > 0 and right > 0:
                row_cnt += 1

    return row_cnt

