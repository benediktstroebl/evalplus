
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
    # Method 1: DP
    # Time O(n*m)
    # Space O(n*m)
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    if capacity == 0 or rows == 1:
        return 0
    res = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # init res
    for i in range(rows):
        for j in range(cols):
            res[i][j] = 0 if grid[i][j] == 0 else math.ceil(capacity / grid[i][j])
    
    # init res
    for i in range(rows):
        for j in range(cols):
            res[i][j] = 0 if grid[i][j] == 0 else math.ceil(capacity / grid[i][j])
    
    # use res
    for i in range(1, rows):
        for j in range(1, cols):
            res[i][j] = max(res[i-1][j], res[i][j-1])
    
    # count res
    count = 0
    for j in range(cols):
        count += res[rows-1][j]
    return count
