
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
    m, n = len(grid), len(grid[0])
    print(m, n)
    row_with_max_water = [[0] * n for _ in range(m)]
    row_with_max_water[0][0] = grid[0][0]
    for i in range(1, m):
        row_with_max_water[i][0] = row_with_max_water[i-1][0] + grid[i][0]

    for j in range(1, n):
        row_with_max_water[0][j] = row_with_max_water[0][j-1] + grid[0][j]
    
    for r in range(1, m):
        for k in range(1, n):
            row_with_max_water[r][k] = max(row_with_max_water[r-1][k], row_with_max_water[r][k-1]) + grid[r][k]

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and row_with_max_water[i][j] >= capacity:
                res += 1

    return res
