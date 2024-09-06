
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
    m = grid[0].length
    filled = [[0] * (m+1) for _ in range(n)]
    bucket_index = [0] * m

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                filled[i][j] = max(filled[i][j], capacity)
                if filled[i][j] > 0:
                    for k in range(m):
                        bucket_index[k] = max(bucket_index[k], filled[i][k] + filled[i][j])
                    if bucket_index[0] >= bucket_index[1]:
                        break
                    for k in range(1, m):
                        if bucket_index[k] >= bucket_index[k+1]:
                            break
    return n - 1