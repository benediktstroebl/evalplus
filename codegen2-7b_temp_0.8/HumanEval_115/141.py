
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
    if not grid or not capacity:
        return 0
    m = len(grid)
    n = len(grid[0])
    taken = [[False for i in range(n)] for j in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not taken[i][j]:
                ans += 1
                taken[i][j] = True
                cur = i
                while cur < m:
                    taken[cur][j] = True
                    cur += 1
    return math.ceil(capacity / (n - 1) * (m - 1) - ans)
    
    
