
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
    R = len(grid)
    C = len(grid[0])
    
    buckets = [[0] * (C+1) for i in range(R+1)]
    for row in range(R):
        for col in range(C):
            buckets[row+1][col+1] = buckets[row+1][col] + grid[row][col]

    res = 0
    for row in range(R+1):
        for col in range(C+1):
            max_well = int(math.floor(capacity / buckets[row][col]))
            res += min(buckets[row][col], max_well)
            buckets[row][col] -= max_well
    return res
