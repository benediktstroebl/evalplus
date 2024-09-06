
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
    import math
    """
    Runtime: 56 ms, faster than 64.47% of Python3 online submissions for Maximal Flow.
    Memory Usage: 13.1 MB, less than 21.11% of Python3 online submissions for Maximal Flow.
    """
    m = len(grid)
    n = len(grid[0])
    dp = [0] * n
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] += 1
    cur = 0
    for i in range(n):
        if dp[i] < capacity:
            cur += 1
    return cur - math.
